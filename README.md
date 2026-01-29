# 📄 PDF Q&A Chatbot using RAG (Gemini + LangChain + FAISS)

A **Retrieval-Augmented Generation (RAG)** based PDF Question Answering system that allows users to ask questions from a PDF document and get **accurate, context-aware answers** using **Google Gemini**, **LangChain**, and **FAISS**, with a **Streamlit UI and streaming responses**.

This project demonstrates a **production-style GenAI pipeline**, not just a demo.

---

## 🚀 Features

- 📄 Load and process PDF documents
- ✂️ Intelligent text chunking with overlap
- 🧠 Vector storage using FAISS
- 🔍 Semantic search using embeddings
- 🤖 Gemini-powered answers (grounded in PDF content)
- 🔄 Retrieval-Augmented Generation (RAG)
- 💬 Chat-style Streamlit UI
- ⚡ Streaming responses (ChatGPT-like typing)
- 🔐 Secure API key handling using `.env`

---

## 🧠 How RAG Works (High-Level)

PDF Document
↓
Text Chunking
↓
Gemini Embeddings
↓
FAISS Vector Store
↓
User Question
↓
Similarity Search
↓
Relevant Context
↓
Gemini LLM
↓
Answer (Streamed)
