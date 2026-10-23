"""Validate the static dossier and its links without network dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1] / 'dist'
PAGES = ['index.html', 'overview.html', 'screenshots.html', 'beta.html']
REPO = 'https://github.com/GreyDoorRepublik/Floppy144-beta'

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.tags = []
        self.ids = set()
        self.links = []
        self.h1 = 0
        self.current = []
        self.canonical = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'{self.path.name}: duplicate ID'
            self.ids.add(attrs['id'])
        for key in ['href', 'src']:
            if key in attrs:
                self.links.append(attrs[key])
        if tag == 'h1':
            self.h1 += 1
        if tag == 'a' and attrs.get('aria-current') == 'page':
            self.current.append(attrs['href'])
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical.append(attrs['href'])
        if tag == 'img':
            assert attrs.get('alt'), 'Screenshot must have descriptive alt text'
            assert attrs.get('width') and attrs.get('height'), 'Image dimensions missing'

pages = {file: Page(ROOT / file) for file in PAGES}
for file, page in pages.items():
    assert page.h1 == 1, f'{file}: expected one h1'
    assert page.current == [file], f'{file}: current navigation is incorrect'
    assert page.canonical == ['https://greydoorrepublik.github.io/floppy144/' + ('' if file == 'index.html' else file)]
    assert any(tag == 'html' and attrs.get('lang') == 'en-GB' for tag, attrs in page.tags)
    assert any(tag == 'meta' and attrs.get('name') == 'viewport' for tag, attrs in page.tags)
    assert not any(tag == 'script' for tag, attrs in page.tags)
    assert 'main' in page.ids
    assert 'https://greydoorrepublik.github.io/' in page.links
    assert REPO in page.links
    assert REPO + '/issues' in page.links
    for url in page.links:
        parts = urlsplit(url)
        if parts.scheme or parts.netloc:
            assert parts.scheme == 'https', f'Insecure URL: {url}'
            continue
        assert not parts.path.startswith('/'), f'Root path breaks subdirectory hosting: {url}'
        target = page.path if not parts.path else page.path.parent / unquote(parts.path)
        assert target.is_file(), f'{file}: missing local target {url}'
        if parts.fragment:
            destination = pages[target.name]
            assert parts.fragment in destination.ids, f'{file}: missing anchor {url}'
assert REPO + '/releases' in pages['beta.html'].links
assert any(url.startswith(REPO + '/issues/new?') for url in pages['beta.html'].links)
assert (ROOT / '.nojekyll').is_file()
assert 'IMAGE NOT YET FILED' not in (ROOT / 'screenshots.html').read_text()
assert 'VISUAL EVIDENCE PENDING' not in (ROOT / 'index.html').read_text()
gallery_images = [attrs for tag, attrs in pages['screenshots.html'].tags if tag == 'img']
assert len(gallery_images) == 7, 'Expected seven selected beta captures'
assert len({image['src'] for image in gallery_images}) == 7, 'Gallery repeats a capture'
assert len([1 for tag, attrs in pages['index.html'].tags if tag == 'img']) == 1
for image in gallery_images:
    raw = (ROOT / image['src']).read_bytes()
    assert raw[:8] == b'\x89PNG\r\n\x1a\n', 'Invalid PNG signature'
    width = int.from_bytes(raw[16:20], 'big')
    height = int.from_bytes(raw[20:24], 'big')
    assert (width, height) == (int(image['width']), int(image['height'])), 'Image dimensions differ from HTML'
    assert image['src'] in pages['screenshots.html'].links, 'Missing full-size image destination'
print('PASS: four pages, links, fragments, navigation, metadata, repository links, seven distinct PNG captures, image dimensions and full-size image paths.')
