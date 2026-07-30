# 📄 AI RAG Document Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot built with **Python**, **Streamlit**, **OpenRouter**, **Sentence Transformers**, and **FAISS**.

Upload PDF, Microsoft Word, or Excel documents and ask natural language questions. The chatbot retrieves the most relevant document sections using semantic search before generating accurate answers with an LLM.

---

## 🚀 Features

- 📄 Upload PDF documents
- 📝 Upload Microsoft Word (.docx)
- 📊 Upload Microsoft Excel (.xlsx)
- 🤖 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic Search using Sentence Transformers
- ⚡ FAISS Vector Database
- 💬 Interactive Chat UI
- 📚 Retrieved Context Viewer
- 🔐 Secure API Key Management
- ☁️ Ready for Streamlit Community Cloud deployment

---

## 🛠 Tech Stack

- Python 3.11+
- Streamlit
- OpenRouter
- OpenAI Python SDK
- Sentence Transformers
- FAISS
- LangChain Text Splitters
- PyPDF
- python-docx
- Pandas

---

## 📂 Project Structure

```text
AI-RAG-Document-Chatbot/
│
├── app.py
├── config.py
├── document_loader.py
├── text_splitter.py
├── embeddings.py
├── vector_store.py
├── rag.py
│
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

## ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/AI-RAG-Document-Chatbot.git

cd AI-RAG-Document-Chatbot
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure OpenRouter

Create a `.env` file.

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser.

```
http://localhost:8501
```

---

## 📄 Supported File Types

- PDF
- DOCX
- XLSX

---

## 🧠 How It Works

```text
Upload Document
        │
        ▼
Extract Text
        │
        ▼
Split into Chunks
        │
        ▼
Generate Embeddings
        │
        ▼
Build FAISS Index
        │
        ▼
User Question
        │
        ▼
Question Embedding
        │
        ▼
Similarity Search
        │
        ▼
Top Relevant Chunks
        │
        ▼
OpenRouter LLM
        │
        ▼
Answer
```

---

## 📦 Dependencies

```text
streamlit
openai
python-dotenv
sentence-transformers
faiss-cpu
langchain-text-splitters
pypdf
python-docx
pandas
openpyxl
```

---

## 📷 Screenshots

### Upload Document

Upload a PDF, DOCX, or XLSX file.

### Ask Questions

Ask questions in natural language.

Example:

```
What is the refund policy?

How many leave days are allowed?

Summarize the uploaded document.
```

### Retrieved Context

Expand **Retrieved Context** to inspect the chunks used to generate the answer.

---

## 🌟 Future Improvements

- ✅ Multiple document support
- ✅ Persistent FAISS database
- ✅ Streaming responses
- ✅ Conversation memory
- ✅ Source citations with page numbers
- ✅ OCR for scanned PDFs
- ✅ Hybrid Search (BM25 + Vector Search)
- ✅ Metadata filtering
- ✅ Drag & Drop upload
- ✅ Docker support
- ✅ Authentication

---

## 🚀 Deployment

The application can be deployed to:

- Streamlit Community Cloud
- Hugging Face Spaces
- Render
- Railway
- Azure App Service
- Google Cloud Run
- AWS EC2
- DigitalOcean

---

## 🤝 Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss the proposed improvements.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Ashish Sharma**

Software Developer | AI Enthusiast

Built with ❤️ using Streamlit, FAISS, Sentence Transformers, and OpenRouter.