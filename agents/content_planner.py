from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os
import re

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 出力フォルダ
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

# topics.txt を読む
with open("topics.txt", "r", encoding="utf-8") as f:
    topics = [line.strip() for line in f if line.strip()]

print(f"{len(topics)} topics found.\n")

for topic in topics:

    print(f"Generating: {topic}")

    prompt = f"""
Create Pinterest content for this topic.

Topic:
{topic}

Return exactly:

Title:
Description:
Keywords:
"""

    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    result = response.output_text

    # ファイル名を作る
    filename = re.sub(r"[^a-zA-Z0-9]+", "_", topic.lower()).strip("_")

    with open(output_dir / f"{filename}.md", "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Saved: {filename}.md")

print("\nAll topics completed!")