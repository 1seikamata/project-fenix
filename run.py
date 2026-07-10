import subprocess
import sys

steps = [
    "agents/content_planner.py",
    "agents/image_generator.py",
    "agents/csv_exporter.py"
]

for step in steps:
    print(f"\n{'=' * 50}")
    print(f"Running: {step}")
    print(f"{'=' * 50}\n")

    result = subprocess.run([sys.executable, step])

    if result.returncode != 0:
        print(f"\nError while running {step}")
        break

print("\nProject FENIX completed!")