from pathlib import Path

RULEBOOK_PATH = Path("data/rulebook.md")


def load_rulebook():
    text = RULEBOOK_PATH.read_text(encoding="utf-8")

    print("Rulebook loaded successfully!")
    print("Characters:", len(text))
    print("Words:", len(text.split()))

    return text


if __name__ == "__main__":
    load_rulebook()