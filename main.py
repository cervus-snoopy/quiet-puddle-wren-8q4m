"""One Line, Zero Use: writes a single useless-superpower line to /output/entry.txt."""
import os

LINE = "I can turn into a puddle at will. I cannot turn back."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
