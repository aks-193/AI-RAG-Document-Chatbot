from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def embed_documents(self, chunks):

        return self.model.encode(
            chunks,
            convert_to_numpy=True,
            show_progress_bar=True,
        )

    def embed_query(self, query):

        return self.model.encode(
            query,
            convert_to_numpy=True,
        )