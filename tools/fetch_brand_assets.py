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
    'comap-application-marine-pms.webp': 'https://imgproc.comap-control.com/Local/mediacontainer/comap/media/marine/comap_ac_pms_marine_scheme_web.png?f=WebP&w=900&h=900',
    'comap-application-standby.webp': 'https://imgproc.comap-control.com/Local/mediacontainer/comap/media/applications/power%20generation/standby/comap-standby-power-example.png?f=WebP&w=900&h=900',
    'comap-application-hybrid.webp': 'https://imgproc.comap-control.com/Local/mediacontainer/comap/media/widgets/application%20example/asset-3microgrid_on_grid.png?f=WebP&w=900&h=900',
    'noris-temperature-sensors.webp': 'https://www.noris-group.com/fileadmin/_processed_/0/6/csm_Tempsens_schiffbau_img_bearb__002_8b3dc21fe0.webp',
    'noris-pressure-sensor.webp': 'https://www.noris-group.com/fileadmin/_processed_/c/7/csm_PAx9_bearb__005_43746a0fad.webp',
    'noris-norimeter.webp': 'https://www.noris-group.com/fileadmin/_processed_/5/3/csm_NIQ3-096-FD1-768-MED-blau_bearb_001_44e1a717ad.webp',
    'noris-signal-processing.webp': 'https://www.noris-group.com/fileadmin/_processed_/4/a/csm_Signalverarbeitung_kombi_img_bearb__006_fefe637b76.webp',
    'noris-norimos.webp': 'https://www.noris-group.com/fileadmin/_processed_/3/2/csm_Bildschirm-mit-NORIMOS4-Visualisierung_2_40d53d7005.webp',
    'noris-noristar.webp': 'https://www.noris-group.com/fileadmin/_processed_/e/a/csm_NORISTAR-4-Panel_img_009_fe9987abc9.webp',
    'comap-intelidrive-700-marine.webp': 'https://imgproc.comap-control.com/Local/mediacontainer/comap/media/products/intelidrive%20700%20marine/inelidrive_700_marine_main.png?f=WebP&w=768&h=768',
    'comap-inteligen-1000-marine.webp': 'https://imgproc.comap-control.com/Local/shp-media-files/comap/media/shpmediafiles/parallel%20gen-set%20controllers/inteligen/web%20images/ig1000%20marine/comap_inteligen_1000_marine-front.png?f=WebP&w=768&h=768',
    'comap-intelilite-4-amf-25.webp': 'https://imgproc.comap-control.com/Local/shp-media-files/comap/media/shpmediafiles/single%20gen-set%20controllers/intelilite/web%20images/optimized%20intelilite/intelilite4_amf25_main.png?f=WebP&w=768&h=768',
    'comap-inteliscada.webp': 'https://imgproc.comap-control.com/Local/shp-media-files/comap/media/shpmediafiles/common%20products/sw%20tools/web%20images/inteliscada%20screen.png?f=WebP&w=768&h=768',
    'comap-websupervisor.webp': 'https://imgproc.comap-control.com/Local/shp-media-files/comap/media/shpmediafiles/common%20products/sw%20tools/web%20images/websupervisor.png?f=WebP&w=768&h=768',
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
