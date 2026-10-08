"""Fetch manufacturer product images used in the review preview.

These are real manufacturer images, not Araya installation photographs.
Source pages and attribution are recorded in docs/CONTENT-SOURCES.md.
This is an optional maintenance command, not part of the Pages build.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen

DEST = Path(__file__).resolve().parents[1] / 'public/assets/images'
ASSETS = {
    'noris-speed-sensors.webp': 'https://www.noris-group.com/fileadmin/_processed_/d/d/csm_FAxx_Kombination_bearb_035_08fc5f7a85.webp',
    'comap-inteligen-500-g2.webp': 'https://imgproc.comap-control.com/Local/shp-media-files/comap/media/shpmediafiles/parallel%20gen-set%20controllers/inteligen/web%20images/optimized%20web%20images/ineligen_500_g2_main.png?f=WebP&h=650&w=850',
}

def fetch(item):
    name, url = item
    with urlopen(Request(url, headers={'User-Agent':'Mozilla/5.0'}), timeout=45) as response:
        data = response.read()
    if data[:4] != b'RIFF' or data[8:12] != b'WEBP':
        raise ValueError(f'Expected WebP image for {name}')
    (DEST / name).write_bytes(data)
    return f'{name}: {len(data):,} bytes'

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as pool:
        for result in pool.map(fetch, ASSETS.items()):
            print(result)
