import streamlit as st

from document_loader import load_document
from text_splitter import split_document
from embeddings import EmbeddingModel
from vector_store import VectorStore
from rag import RAGChatbot

st.set_page_config(
    page_title="AI RAG Document Chatbot",
    page_icon="📄",
)

st.title("📄 AI RAG based Document Chatbot")

# -----------------------
# Session State
# -----------------------

if "rag" not in st.session_state:
    st.session_state.rag = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------
# Upload
# -----------------------

uploaded_file = st.file_uploader(
    "Upload PDF/DOCX/XLSX",
    type=["pdf", "docx", "xlsx"]
)

if uploaded_file and st.session_state.rag is None:

    with st.spinner("Indexing document..."):

        document = load_document(uploaded_file)

        chunks = split_document(document)

        embedding_model = EmbeddingModel()

        embeddings = embedding_model.embed_documents(chunks)

        vector_store = VectorStore()

        vector_store.build(
            embeddings,
            chunks
        )

        st.session_state.rag = RAGChatbot(
            vector_store,
            embedding_model
        )

    st.success("Document indexed successfully.")

# -----------------------
# Chat History
# -----------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# -----------------------
# Chat
# -----------------------

if st.session_state.rag:

    question = st.chat_input(
        "Ask anything about your document..."
    )

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.spinner("Thinking..."):

            answer, sources = st.session_state.rag.ask(question)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message("assistant"):

            st.markdown(answer)

            # with st.expander("Retrieved Context"):

            #     for i, item in enumerate(sources, start=1):

            #         st.markdown(f"### Chunk {i}")
            #         st.write(item["chunk"])
            #         st.caption(f"Distance: {item['distance']:.4f}")
            #         st.divider()