from config import client, MODEL


class RAGChatbot:

    def __init__(self, vector_store, embedding_model):
        self.vector_store = vector_store
        self.embedding_model = embedding_model

    def ask(self, question):

        query_embedding = self.embedding_model.embed_query(question)

        retrieved_chunks = self.vector_store.search(
            query_embedding,
            k=3
        )
        
        context = "\n\n".join(
            item["chunk"] for item in retrieved_chunks
        )

        prompt = f"""
You are an AI assistant.

Answer ONLY from the provided context.

If the answer is not present,
reply:

"I couldn't find the answer in the uploaded document."

Context:
{context}

Question:
{question}
"""

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response.choices[0].message.content

        return answer, retrieved_chunks