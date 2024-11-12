from PIL import Image
import pytesseract
import requests
from io import BytesIO


def parse(gif_url):
    response = requests.get(gif_url)
    gif = Image.open(BytesIO(response.content))
    first_frame = gif.copy()
    text = pytesseract.image_to_string(first_frame)

    return (
        text
        .replace("\n", "")
    )
