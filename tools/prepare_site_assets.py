"""Prepare client logos, responsive photo variants, the share image and the proportioned logo.

Client logos come from the owner's live website uploads. Run from the repository root:
    python tools/prepare_site_assets.py
"""
from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen
from PIL import Image, ImageChops

IMAGES = Path(__file__).resolve().parents[1] / "public" / "assets" / "images"
UPLOADS = "https://arayainternusa.co.id/araya/wp-content/uploads/2026/04/"
# file on the live site -> (output name, optional crop box removing captions)
CLIENT_LOGOS = {
    "pelni.png": ("client-pelni.webp", (0, 0, 234, 90)),
    "pelindo.png": ("client-pelindo.webp", None),
    "pertamina-1.png": ("client-pertamina.webp", None),
    "tni.png": ("client-tni-al.webp", None),
    "PT-armada-cakrawala-esa.png": ("client-armada-cakrawala-esa.webp", None),
    "usda2.png": ("client-usda-seroja-jaya.webp", None),
}
# Owner photos carry a camera date stamp in the bottom 60px; the web variants crop it away.
RESPONSIVE = {"ship.webp": (800, 1400), "control-room.webp": (800, 1400)}
STAMP_FREE_HEIGHT = 784


def fetch(url):
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=30) as response:
        return response.read()


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


def client_logos():
    for source, (name, crop) in CLIENT_LOGOS.items():
        image = Image.open(BytesIO(fetch(UPLOADS + source)))
        if crop:
            image = image.crop(crop)
        image = trim(white_to_alpha(image))
        if image.height > 96:
            image = image.resize((round(image.width * 96 / image.height), 96), Image.LANCZOS)
        image.save(IMAGES / name, "WEBP", quality=90, method=6)
        print(f"{name}: {image.size}")


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
    client_logos()
    responsive_variants()
    share_image()
    proportioned_logo()
    print("Client logos, responsive variants, share image and proportioned logo prepared.")
