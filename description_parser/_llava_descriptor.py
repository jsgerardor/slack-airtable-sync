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

def parse(gif_url):
    url = "http://172.20.40.11:8000/v1/chat/completions"
    payload = {
        "model": "llava-v1.5-7b",
        "temperature": 0,
        "messages": [
            {
                "content": "You extract text from image and you only extract what the user tells you",
                "role": "system"
            },
            {
                "content": [
                    {
                        "type": "text",
                        "text": _PROMPT
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": gif_url
                        }
                    }
                ],
                "role": "user"
            }
        ]
    }

    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }

    response = requests.post(url, headers=headers, json=payload)
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
