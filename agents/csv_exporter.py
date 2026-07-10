from pathlib import Path
import csv
import re

output_dir = Path("output")
csv_file = "pinterest_posts.csv"

rows = []

for md in output_dir.glob("*.md"):

    text = md.read_text(encoding="utf-8")

    def find(label):
        m = re.search(rf"{label}:\s*(.*?)(?:\n\n|\Z)", text, re.S)
        return m.group(1).replace("\n", " ").strip() if m else ""

    title = find("Title")
    description = find("Description")
    keywords = find("Keywords")
    image_prompt = find("Image Prompt")

    rows.append([
        md.stem + ".png",
        title,
        description,
        keywords,
        image_prompt
    ])

with open(csv_file, "w", newline="", encoding="utf-8-sig") as f:

    writer = csv.writer(f)

    writer.writerow([
        "Image",
        "Title",
        "Description",
        "Keywords",
        "Image Prompt"
    ])

    writer.writerows(rows)

print(f"Saved {csv_file}")