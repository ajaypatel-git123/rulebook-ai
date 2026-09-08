# Rulebook AI

An AI-powered Rulebook Question Answering system that can identify:

- ANSWERED
- NOT COVERED
- CONFLICT

The system retrieves relevant sections from a university rulebook and uses AI reasoning to generate evidence-based answers without relying on outside knowledge.

## Tech Stack

- Python
- FastAPI
- Sentence Transformers
- FAISS
- Groq API
- Pydantic
- NumPy
- HTML / CSS / JavaScript

## How It Works

Question
↓
Sentence Transformer Embedding
↓
FAISS Semantic Search
↓
Relevant Rulebook Evidence
↓
Groq AI Reasoning
↓
Classification + Answer + Citations

## Classifications

### ANSWERED
The rulebook contains sufficient information to answer the question.

### NOT COVERED
The rulebook does not contain information required to answer the question.

### CONFLICT
The rulebook contains contradictory rules that apply to the question.

## Project Structure

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