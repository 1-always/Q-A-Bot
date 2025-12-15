

## **README.md**

# 🧠 RAG Q&A Support Bot

This project is a **Retrieval-Augmented Generation (RAG)** pipeline that builds an intelligent **Q&A support bot** using your website’s content.

It crawls a website, cleans the text, generates embeddings, stores them in a **vector database (FAISS)**, and exposes a **FastAPI endpoint** that answers user questions **only from the crawled content**.

---

## 🚀 Features

✅ Crawl and extract text content from any website
✅ Clean and chunk text into manageable pieces
✅ Generate text embeddings using OpenAI models
✅ Store embeddings in a FAISS vector database for fast similarity search
✅ Retrieve relevant chunks based on user queries
✅ Use a language model to answer questions grounded in retrieved content
✅ Expose an API endpoint (`/ask`) to integrate the bot anywhere (chat, UI, etc.)

---

## 🧩 Project Structure

```
rag_bot/
│
├── crawler.py            # Crawl website and save raw text
├── clean_text.py         # Clean text and split into chunks
├── embeddings.py         # Generate embeddings for text chunks
├── vector_store.py       # Store embeddings in FAISS
├── retriever.py          # Retrieve relevant chunks and generate answers
├── api.py                # FastAPI endpoint for Q&A
├── requirements.txt      # Python dependencies
└── data/
    ├── raw_text.json         # Crawled website text
    ├── embeddings.json       # Embeddings for chunks
    ├── embeddings.index      # FAISS index file
    └── index_to_chunk.json   # Mapping of index -> text chunks
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/rag-bot.git
cd rag-bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Set your OpenAI API key as an environment variable:

**Linux/macOS:**

```bash
export OPENAI_API_KEY="your_api_key_here"
```

**Windows (PowerShell):**

```bash
setx OPENAI_API_KEY "your_api_key_here"
```

---

## 🧱 Step-by-Step Workflow

### **1️⃣ Crawl the Website**

Edit `crawler.py` and add your target URLs:

```python
urls = [
    "https://example.com",
    "https://example.com/about"
]
```

Then run:

```bash
python crawler.py
```

➡️ This will create `data/raw_text.json` containing the website’s text.

---

### **2️⃣ Clean and Chunk Text**

```bash
python clean_text.py
```

➡️ This removes unwanted characters and splits text into smaller chunks.

---

### **3️⃣ Generate Embeddings**

```bash
python embeddings.py
```

➡️ Uses OpenAI’s embedding model (`text-embedding-3-small`) to create vector representations of each chunk.

---

### **4️⃣ Build the Vector Store**

```bash
python vector_store.py
```

➡️ Stores all embeddings in a **FAISS** index for fast retrieval.

---

### **5️⃣ Run the API**

```bash
python api.py
```

This starts a FastAPI server at:

👉 [http://127.0.0.1:8000/ask](http://127.0.0.1:8000/ask)

---

### **6️⃣ Ask Questions**

Use `curl` or Postman to send questions:

```bash
curl -X POST "http://127.0.0.1:8000/ask" \
-H "Content-Type: application/json" \
-d '{"question":"What is this website about?"}'
```

**Example Response:**

```json
{
  "answer": "This website provides tutorials and guides about..."
}
```

---

## ⚡ Example Use Cases

* Support bot for your company’s documentation site
* Knowledge retrieval system for internal portals
* FAQ assistant for your product website
* Conversational interface for static HTML documentation

---

## 🧠 How It Works (RAG Pipeline)

1. **Crawling** → Collects website content
2. **Preprocessing** → Cleans and chunks text
3. **Embedding** → Converts text to vector form
4. **Vector Store** → Stores and searches text semantically
5. **Retrieval + Generation** → Combines search results with LLM responses

---

## 🧰 Tech Stack

| Component        | Technology           |
| ---------------- | -------------------- |
| Language         | Python 3.10+         |
| Web Framework    | FastAPI              |
| Vector Database  | FAISS                |
| LLM & Embeddings | OpenAI API           |
| Data Processing  | BeautifulSoup, NumPy |

---

## 🔍 Troubleshooting

* **Low-quality answers?**

  * Try smaller chunks (e.g., 300–500 tokens).
  * Use a better model like `gpt-4.1` for answer generation.

* **API key not found?**

  * Check your environment variable setup.

* **Unicode errors in crawling?**

  * Add `.encode('utf-8', errors='ignore').decode('utf-8')` while saving text.

---

## 🌟 Future Enhancements

* Support for multi-page crawling (automatic link traversal)
* Integration with Pinecone or Chroma DB
* Streamlit or React frontend
* Context caching for faster responses
* Support for file uploads (PDFs, docs)

---


