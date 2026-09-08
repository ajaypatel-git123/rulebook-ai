from pathlib import Path
import re

RULEBOOK_PATH = Path("data/rulebook.md")


def load_rulebook():
    return RULEBOOK_PATH.read_text(encoding="utf-8")


def create_chunks(text):
    sections = re.split(r"\n(?=# \d+\.)", text)

    chunks = []

    for section in sections:
        section = section.strip()

        if not section:
            continue

        lines = section.splitlines()
        title = lines[0].replace("# ", "").strip()
        content = "\n".join(lines[1:]).strip()

        if content:
            chunks.append({
                "title": title,
                "text": content
            })

    return chunks


if __name__ == "__main__":
    text = load_rulebook()
    chunks = create_chunks(text)

    print("Total chunks:", len(chunks))

    for i, chunk in enumerate(chunks[:5]):
        print(f"\n--- Chunk {i} ---")
        print("Title:", chunk["title"])
        print("Characters:", len(chunk["text"]))