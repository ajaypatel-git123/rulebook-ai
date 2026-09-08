import faiss
import numpy as np

from app.embedder import model
from chunker import load_rulebook, create_chunks


INDEX_PATH = "index/rulebook.faiss"

# Number of results we retrieve
TOP_K = 5


# Load rulebook and chunks
text = load_rulebook()
chunks = create_chunks(text)

# Load FAISS index
index = faiss.read_index(INDEX_PATH)


def search(query, top_k=TOP_K):

    # Convert user query into embedding
    query_embedding = model.encode(
        [query],
        normalize_embeddings=True
    )

    query_embedding = np.asarray(
        query_embedding,
        dtype="float32"
    )

    # Search FAISS
    scores, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for score, idx in zip(scores[0], indices[0]):

        # Ignore generic final interpretation section
        if chunks[idx]["title"] == "24. Final Interpretive Principles":
            continue

        document = chunks[idx]["text"]

        results.append({
            "score": float(score),
            "title": chunks[idx]["title"],
            "text": document
        })

    return results


if __name__ == "__main__":

    query = input("\nEnter your question: ")

    results = search(query)

    print("\nTop relevant sections:\n")

    for i, result in enumerate(results, start=1):

        print(f"{i}. {result['title']}")
        print(f"Similarity: {result['score']:.4f}")
        print(f"Text: {result['text'][:500]}...")
        print("-" * 80)