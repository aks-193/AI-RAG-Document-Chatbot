import faiss
import numpy as np


class VectorStore:

    def __init__(self):

        self.index = None
        self.chunks = []

    def build(self, embeddings, chunks):
        """
        Build the FAISS index.
        """

        embeddings = np.array(
            embeddings,
            dtype="float32"
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

        self.chunks = chunks

    def search(self, query_embedding, k=3):
        query_embedding = np.array(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = self.index.search(query_embedding, k)

        results = []

        for distance, idx in zip(distances[0], indices[0]):
            results.append({
                "chunk": self.chunks[idx],
                "distance": float(distance),
            })

        return results