from pathlib import Path
import sys

from sentence_transformers import SentenceTransformer

sys.path.append(str(Path(__file__).parent))

from chunker import load_rulebook, create_chunks


MODEL_NAME = "sentence-transformers/multi-qa-MiniLM-L6-dot-v1"

model = SentenceTransformer(MODEL_NAME)


def create_embeddings(chunks):
    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=True
    )

    return embeddings


if __name__ == "__main__":
    text = load_rulebook()
    chunks = create_chunks(text)

    embeddings = create_embeddings(chunks)

    print("Chunks:", len(chunks))
    print("Embeddings:", len(embeddings))
    print("Vector dimensions:", embeddings.shape[1])