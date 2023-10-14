import os
import json
import requests

from base64 import b64decode
from dotenv import load_dotenv
from asgiref.sync import sync_to_async
from src import utils

load_dotenv()
lora_api_url = os.getenv("LORA_API_URL")

# so that subsequent writes don't crash to missing directory
from pathlib import Path
IMAGE_DIR = Path.cwd() / "images"
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

async def draw(prompt: str) -> list[str]:
    payload = {
        "username": "sacabam_bot",
        "image": "none",
        "features": "txt2img",
        "style": "anime",
        "prompt": prompt,
        "param": {}
    }

    # Make the POST request
    response = await sync_to_async(requests.post)(
        lora_api_url,
        json=payload
    )

    image_b64str = response.json()['result_image']
    decoded_image_data = b64decode(image_b64str)

    rel_path = r"images/lora_image_test.png"
    abs_path = utils.get_absolute_path(rel_path)
    with open(abs_path, "wb") as f:
        f.write(decoded_image_data)

    return [abs_path]


if __name__ == "__main__":
    import asyncio
    async def main():
        await draw("cirno")
    asyncio.run(main())
