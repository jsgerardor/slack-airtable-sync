import base64
import json

from PIL import Image
import requests
from io import BytesIO

_PROMPT = """
This image is the final result of someone giving a reward to a person.The reward is named "karma". This is the description of the contents of the image:
- A big image of the person who got the karmas
- Next to the image the name of the person
- Next to the name of the person a plus sign and the number of karmas given to that person
- Below that You'll find the information of the person who gave karmas
- Below the information of the person who gave the karmas you'll find the "reason" the person who gave karmas is using to reward the person who received the karmas
- at the bottom right you'll find a funny image
Your task:
Reply only once the text representing the "reason". Do not add extra explanation, just the reason
"""


def _download_image(gif_url):
    response = requests.get(gif_url)
    gif = Image.open(BytesIO(response.content))
    gif.seek(0)

    buffered = BytesIO()
    gif.save(buffered, format="PNG")
    buffered.seek(0)

    return base64.b64encode(buffered.read()).decode('utf-8')

# TODO: Change this to use an API instead of local
def parse(gif_url):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llava",
        "prompt": _PROMPT,
        "images": [_download_image(gif_url)]
    }

    response = requests.post(url, json=payload)
    generated_texts = [line for line in response.text.split('\n')]

    description = ""
    for text in generated_texts:
        try:
            description += json.loads(text)["response"]
        except json.JSONDecodeError:
            pass

    return (
        description
        .strip()
    )
