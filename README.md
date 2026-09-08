# 📘 Rulebook AI

> **AI-powered Rulebook Question Answering System**  
> Ask questions about a university rulebook and get **evidence-based answers with source citations**.

Rulebook AI uses **RAG (Retrieval-Augmented Generation)** to retrieve relevant sections from a university rulebook before using an LLM for reasoning. This helps keep answers grounded in the provided rulebook rather than relying on outside knowledge.

## ✨ Classifications

| Classification | Meaning |
|---|---|
| ✅ **ANSWERED** | The rulebook contains sufficient information to answer the question. |
| ⚠️ **NOT COVERED** | The required information is not available in the rulebook. |
| 🔀 **CONFLICT** | Relevant rules contain contradictory information. |

## 🛠️ Tech Stack

- 🐍 **Python**
- ⚡ **FastAPI**
- 🧠 **Sentence Transformers**
- 🔎 **FAISS**
- 🤖 **Groq API**
- ✅ **Pydantic**
- 🔢 **NumPy**
- 🌐 **HTML / CSS / JavaScript**

## 🔄 How It Works

```text
👤 User Question
       ↓
🧠 Sentence Transformer
       ↓
🔎 FAISS Semantic Search
       ↓
📚 Relevant Rulebook Evidence
       ↓
🤖 Groq AI Reasoning
       ↓
🏷️ Classification + Answer + Citations
```

## 🚀 Key Features

- 📚 Semantic search over rulebook content
- 🤖 Evidence-based AI responses
- 🏷️ `ANSWERED / NOT COVERED / CONFLICT` classification
- 📌 Source citations
- ⚡ Fast vector retrieval using FAISS
- 🔌 FastAPI backend
- 🌐 Web-based interface

## 📂 Project Structure

```text
rulebook-ai/
├── app/
├── data/
├── index/
├── static/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd rulebook-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key
```

> 🔐 Never commit your API key or `.env` file to GitHub.

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

## 🧪 Mocked / Simulated Components

This project uses a **fictional university rulebook** created specifically for demonstration and evaluation purposes.

The rulebook contains intentionally planted contradictions to test the system's ability to identify conflicting rules.

The system itself is not mocked:
- ✅ Semantic embeddings are generated using Sentence Transformers
- ✅ FAISS performs the actual vector similarity search
- ✅ Groq API performs the actual LLM reasoning
- ✅ FastAPI serves the actual backend
- ✅ Classification is generated from retrieved rulebook evidence

No external university database or production university policy system is connected.

## 🎯 Project Goal

Rulebook AI is designed to make university rules easier to query while keeping responses **grounded in the official rulebook evidence**.

---


