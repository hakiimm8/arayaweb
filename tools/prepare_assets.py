"""Prepare public media from an owner-supplied WordPress uploads directory."""
import argparse
from pathlib import Path
import re
import shutil
from urllib.request import Request, urlopen
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1] / "public" / "assets"
MEDIA = {
    "ship.webp": "2026/04/slide2.png",
    "control-room.webp": "2026/04/slide1.png",
    "team.webp": "2026/04/Desain-tanpa-judul.jpg.jpeg",
    "marine.webp": "2026/04/Perkapalan.jpg",
    "industrial.webp": "2024/03/Industrial-1.jpg",
}


def fetch(url):
    request = Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"})
    with urlopen(request, timeout=30) as response:
        return response.read()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("uploads", type=Path)
    args = parser.parse_args()
    images = ROOT / "images"
    fonts = ROOT / "fonts"
    images.mkdir(parents=True, exist_ok=True)
    fonts.mkdir(parents=True, exist_ok=True)
    for filename, relative in MEDIA.items():
        source = args.uploads / relative
        with Image.open(source) as original:
            image = ImageOps.exif_transpose(original).convert("RGB")
            image.thumbnail((1400, 1400))
            image.save(images / filename, "WEBP", quality=84, method=6)
        print(f"{filename}: {source.stat().st_size} -> {(images / filename).stat().st_size} bytes")
    shutil.copyfile(args.uploads / "2026/04/logo3.png", images / "araya-logo.png")
    shutil.copyfile(args.uploads / "2026/04/fav.png", images / "favicon.png")
    css = fetch("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&display=swap").decode()
    urls = re.findall(r"url\((https://fonts\.gstatic\.com/[^)]+\.woff2)\)", css)
    if not urls:
        raise RuntimeError("No WOFF2 font found in official Google Fonts response")
    # Google Fonts lists the latin subset last.
    (fonts / "space-grotesk.woff2").write_bytes(fetch(urls[-1]))
    (fonts / "OFL.txt").write_bytes(fetch("https://raw.githubusercontent.com/google/fonts/main/ofl/spacegrotesk/OFL.txt"))
    print("Original logo, favicon, locally hosted Space Grotesk and license prepared.")


if __name__ == "__main__":
    main()
