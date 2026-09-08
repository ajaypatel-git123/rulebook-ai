import faiss
import numpy as np

from embedder import create_embeddings
from chunker import load_rulebook, create_chunks


def build_index():
    text = load_rulebook()
    chunks = create_chunks(text)

    embeddings = create_embeddings(chunks)
    embeddings = np.asarray(embeddings, dtype="float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)

    faiss.write_index(index, "index/rulebook.faiss")
    np.save("index/embeddings.npy", embeddings)

    print("FAISS index built successfully!")
    print("Vectors:", index.ntotal)
    print("Dimensions:", dimension)


if __name__ == "__main__":
    build_index()