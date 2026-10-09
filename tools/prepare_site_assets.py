"""Prepare client logos, responsive photo variants, the share image and the proportioned logo.

Run from the repository root:
    python tools/prepare_site_assets.py [--cache DIR]

Client logos use the best available source: Wikimedia files (official vector logos or
high-resolution renders) where they exist, otherwise the owner's live-website uploads.
Wikimedia rate-limits shared networks, so downloads retry with backoff; --cache keeps
raw downloads between runs. Sources are recorded in docs/CONTENT-SOURCES.md.
"""
import argparse
import time
from io import BytesIO
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from PIL import Image, ImageChops

IMAGES = Path(__file__).resolve().parents[1] / "public" / "assets" / "images"
UPLOADS = "https://arayainternusa.co.id/araya/wp-content/uploads/2026/04/"
WIKIMEDIA = "https://upload.wikimedia.org/wikipedia/"
# output name -> (source URL, white background to remove)
CLIENT_LOGOS = {
    "client-pelni.webp": (WIKIMEDIA + "commons/thumb/7/7c/PELNI_2023.svg/1280px-PELNI_2023.svg.png", False),
    "client-pertamina.svg": (WIKIMEDIA + "commons/e/e6/Pertamina_Logo.svg", False),
    "client-pelindo.webp": (WIKIMEDIA + "commons/6/69/Logo_Baru_Pelindo_%282021%29.png", False),
    "client-tni-al.webp": (WIKIMEDIA + "commons/thumb/7/79/Insignia_of_the_Indonesian_Navy.svg/330px-Insignia_of_the_Indonesian_Navy.svg.png", False),
    "client-samudera-indonesia.webp": (WIKIMEDIA + "id/1/14/Logo_Samudera_Indonesia_PT.png", False),
    "client-usda-seroja-jaya.webp": (UPLOADS + "usda2.png", True),
    "client-armada-cakrawala-esa.webp": (UPLOADS + "PT-armada-cakrawala-esa.png", True),
}
LOGO_HEIGHT = 160
# Owner photos carry a camera date stamp in the bottom 60px; the web variants crop it away.
RESPONSIVE = {"ship.webp": (800, 1400), "control-room.webp": (800, 1400)}
STAMP_FREE_HEIGHT = 784


def fetch(url, cache=None):
    cached = cache / url.rsplit("/", 1)[-1] if cache else None
    if cached and cached.exists():
        return cached.read_bytes()
    for attempt in range(5):
        try:
            request = Request(url, headers={"User-Agent": "ArayaWebPreview/1.0 (static site build)"})
            with urlopen(request, timeout=30) as response:
                data = response.read()
            break
        except HTTPError as error:
            if error.code != 429 or attempt == 4:
                raise
            time.sleep(15 * (attempt + 1))
    if cached:
        cache.mkdir(parents=True, exist_ok=True)
        cached.write_bytes(data)
    return data


def white_to_alpha(image):
    """Make the flat white logo background transparent, keeping anti-aliased edges soft."""
    image = image.convert("RGBA")
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            distance = 255 - min(r, g, b)
            if distance < 40:
                pixels[x, y] = (r, g, b, int(a * distance / 40))
    return image


def trim(image):
    box = image.getchannel("A").point(lambda v: 255 if v > 12 else 0).getbbox()
    return image.crop(box) if box else image


def client_logos(cache=None):
    for name, (url, white_background) in CLIENT_LOGOS.items():
        data = fetch(url, cache)
        if name.endswith(".svg"):
            (IMAGES / name).write_bytes(data)
            print(f"{name}: vector, {len(data)} bytes")
            continue
        image = Image.open(BytesIO(data)).convert("RGBA")
        image = trim(white_to_alpha(image) if white_background else image)
        if image.height > LOGO_HEIGHT:
            image = image.resize((round(image.width * LOGO_HEIGHT / image.height), LOGO_HEIGHT), Image.LANCZOS)
        image.save(IMAGES / name, "WEBP", quality=92, method=6)
        print(f"{name}: {image.size}")
        time.sleep(3)


def responsive_variants():
    for name, widths in RESPONSIVE.items():
        with Image.open(IMAGES / name) as image:
            image = image.convert("RGB").crop((0, 0, image.width, STAMP_FREE_HEIGHT))
            for width in widths:
                height = round(image.height * width / image.width)
                image.resize((width, height), Image.LANCZOS).save(IMAGES / name.replace(".webp", f"-{width}.webp"), "WEBP", quality=80, method=6)


def share_image():
    """1200x630 JPEG for link previews: owner photo, dark gradient and the original logo on its orange block."""
    with Image.open(IMAGES / "ship.webp") as photo:
        photo = photo.convert("RGB")
        scale = max(1200 / photo.width, 630 / photo.height)
        photo = photo.resize((round(photo.width * scale), round(photo.height * scale)), Image.LANCZOS)
        left, top = (photo.width - 1200) // 2, (photo.height - 630) // 2
        canvas = photo.crop((left, top, left + 1200, top + 630))
    gradient = Image.linear_gradient("L").rotate(90).resize((1200, 630))
    shade = Image.new("RGB", (1200, 630), (14, 17, 22))
    canvas = Image.composite(canvas, shade, ImageChops.multiply(gradient, Image.new("L", (1200, 630), 210)))
    logo = Image.open(IMAGES / "araya-logo.png").convert("RGBA")
    logo = logo.resize((logo.width * 2, logo.height * 2), Image.LANCZOS)
    block = Image.new("RGBA", (logo.width + 64, logo.height + 48), (238, 92, 3, 255))
    block.alpha_composite(logo, (32, 24))
    canvas.paste(block, (72, 72), block)
    canvas.save(IMAGES / "og-araya.jpg", "JPEG", quality=84, optimize=True, progressive=True)


def proportioned_logo():
    """The transparent upload is stretched horizontally; restore the 238:52 lockup ratio without redrawing."""
    with Image.open(IMAGES / "araya-logo-original.png") as logo:
        logo.resize((238, 52), Image.LANCZOS).save(IMAGES / "araya-logo-transparent.png", optimize=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", type=Path, help="directory that keeps raw downloads between runs")
    client_logos(parser.parse_args().cache)
    responsive_variants()
    share_image()
    proportioned_logo()
    print("Client logos, responsive variants, share image and proportioned logo prepared.")
