# AskDocs — Intelligent Document Question Answering

AskDocs is an end-to-end Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and interact with them using natural-language questions.

The system processes documents, converts their content into searchable vector representations, retrieves relevant context, and uses a Large Language Model (LLM) to generate context-aware answers.

## Overview

AskDocs combines document processing, semantic search, vector databases, LLMs, and REST APIs into a single application.

### Architecture

PDF Documents
   ↓
PyMuPDF
   ↓
Text Extraction & Chunking
   ↓
Hugging Face Embeddings
   ↓
ChromaDB
   ↓
Semantic Retrieval
   ↓
LangChain Retrieval Pipeline
   ↓
Groq API (LLM)
   ↓
Context-Aware Answer
   ↓
FastAPI REST API
   ↓
Streamlit Interface

## ✨ Features

- Upload and process PDF documents
- Extract text from PDFs using PyMuPDF
- Split documents into meaningful text chunks
- Generate semantic embeddings using Hugging Face models
- Store and search document embeddings using ChromaDB
- Retrieve relevant document context using LangChain
- Generate context-aware responses using Groq-hosted LLMs
- REST API backend built with FastAPI
- Interactive document-questioning interface using Streamlit
- Metadata-aware document processing and retrieval
- Configurable chunking and retrieval parameters

## 🛠️ Tech Stack

### Core
- Python
- LangChain
- PyMuPDF

### Retrieval & Vector Search
- Hugging Face Embeddings
- ChromaDB
- Semantic Similarity Search

### LLM
- Groq API
- Groq-hosted Large Language Models

### Backend
- FastAPI
- REST API
- Uvicorn

### Frontend
- Streamlit

### Development
- Git
- GitHub
- Python Virtual Environment

## 🧠 RAG Pipeline

AskDocs follows a Retrieval-Augmented Generation architecture:

### 1. Document Ingestion

PDF files are uploaded and processed using PyMuPDF to extract their textual content.

### 2. Text Processing

Extracted text is divided into smaller chunks to make retrieval more precise and provide the LLM with relevant context.

### 3. Embedding Generation

Each text chunk is converted into a numerical vector representation using Hugging Face embedding models.

### 4. Vector Storage

The generated embeddings and associated metadata are stored in ChromaDB, enabling semantic similarity search.

### 5. Retrieval

When a user asks a question, the query is converted into an embedding and compared against the stored document vectors to identify the most relevant chunks.

### 6. Generation

The retrieved context is passed through a LangChain retrieval pipeline to a Groq-hosted LLM, which generates a context-aware response.

## 🔌 REST API

AskDocs exposes its core functionality through a FastAPI REST API.

The API is designed to support workflows such as:

- Document ingestion
- Document processing
- Semantic retrieval
- Question answering

This separates the RAG backend from the user interface and allows the system to be consumed by other applications.

## 📁 Project Structure

```text
AskDocs/
│
├── app/
│   ├── api/
│   ├── ingestion/
│   ├── retrieval/
│   ├── generation/
│   └── ui/
│
├── data/
│
├── chroma_db/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── ...