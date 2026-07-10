from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

client = OpenAI()

output_dir = Path("output")
image_dir = Path("images")

image_dir.mkdir(exist_ok=True)

for file in output_dir.glob("*.md"):

    text = file.read_text(encoding="utf-8")

    if "Image Prompt:" not in text:
        continue

    prompt = text.split("Image Prompt:")[1].strip()

    print(f"Generating image: {file.stem}")

    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1536"
    )

    image_base64 = result.data[0].b64_json

    import base64

    with open(image_dir / f"{file.stem}.png", "wb") as f:
        f.write(base64.b64decode(image_base64))

print("Done!")