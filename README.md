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
```
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
```

---

## 🛠️ Tech Stack

- **Python**
- **Google Gemini (LLM + Embeddings)**
- **LangChain (LCEL, modern APIs)**
- **FAISS** (Vector Database)
- **Streamlit** (UI)
- **python-dotenv** (Environment variables)

---

## 📁 Project Structure
```
PDF_RAG_PROJECT/
│── data/
│ └── sample.pdf
│── vectorstore/
│ ├── index.faiss
│ └── index.pkl
│── ingest.py                     # PDF ingestion & vector creation
│── app.py                        # Streamlit UI + streaming RAG
│── .env                          # API key (ignored by git)
│── .gitignore
│── requirements.txt
│── README.md
```

---

## 🔐 Environment Setup

### 1️⃣ Create a `.env` file

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```
<br>⚠️ Never commit .env to GitHub<br>
Ensure .gitignore contains:
```
.env
```
## 📦 Installation

2️⃣ Install dependencies
```
pip install -r requirements.txt
```
requirements.txt
```
streamlit
python-dotenv
langchain
langchain-core
langchain-community
langchain-google-genai
langchain-text-splitters
faiss-cpu
```
## 🧾 Step 1: Ingest the PDF

This step:
- Loads the PDF
- Splits text into chunks
- Generates embeddings
- Stores vectors in FAISS
```
python ingest.py
```
Expected output:
```
✅ PDF ingested successfully
```
A vectorstore/ folder will be created.

## 💬 Step 2: Run the Chatbot UI
```
streamlit run app.py
```
The app will open in your browser automatically.

## 🧪 Example Questions You Can Ask
Here are good, realistic questions you should try on your PDF Q&A bot (from easy → advanced).

**🔹 Basic Understanding (Warm-up)**

- “What is the main problem this paper is trying to solve?”
- “Summarize the abstract in simple words.”
- “What is the title of this paper?”
- “Who is the author of this paper?”

**👉 These confirm document ingestion is correct.**

**🔹 Conceptual / Technical Questions**

- “What is an Autonomous QA Agent according to the paper?”
- “How does the proposed system use RAG?”
- “Why are LLMs unreliable for Selenium script generation?”
- “What role does retrieval play in reducing hallucination?”

**👉 These test semantic search + context grounding.**

**🔹 Methodology Section (Very Important)**

- “Explain the methodology used in this paper.”
- “What types of documents are ingested into the vector database?”
- “How does the system generate Selenium scripts?”
- “What frameworks or tools are used in the proposed approach?”

**👉 These show deep chunk retrieval, not surface text.**

**🔹 Results & Evaluation (Interview-Level)**

- “What were the evaluation metrics used?”
- “How does the RAG approach compare with a standard LLM?”
- “What accuracy or success rate did the system achieve?”
- “What are the key experimental results?”

**👉 These prove your bot handles numbers + evidence.**

**🔹 Critical Thinking / Insight Questions**

- “What are the limitations of this approach?”
- “What future work is suggested by the authors?”
- “In which scenarios might this system fail?”
- “Why is RAG better than fine-tuning in this case?”

**👉 These separate real RAG from keyword search.**

**🔹 Negative Test (VERY IMPORTANT)**

- “Explain how GPT-4 was trained.”
- “What is the capital of France?”

**✅ Expected answer:**
- “I don’t know.”

This proves:
- Hallucination control
- Prompt discipline
- Production readiness

**🔥 Best Demo Questions (Use These in Interviews)**

If you’re showing this project to someone, ask:

- “How does the Autonomous QA Agent reduce hallucination when generating Selenium scripts?”
- “What evidence does the paper provide that RAG improves execution success?”
These make your project look research-grade.

**🧠 Pro Tip (Important)**

If answers feel weak:

- Increase k from 3 → 5
- Slightly increase chunk overlap
- Ask more specific questions

✅ One-Line Summary

Good RAG questions are specific, document-grounded, and evidence-based.
- What is the main problem this paper addresses?
- Explain the proposed methodology.
- How does RAG improve reliability?
- What evaluation results are reported?
- What are the limitations of this approach?

**❌ Out-of-scope questions (correctly handled):**
- What is the capital of France?
**➡️ Response:**
  
I don’t know.

## 🔥 Key Highlights

- Uses modern LangChain LCEL (no deprecated chains)
- Prevents hallucinations by grounding answers in retrieved context
- Streams responses token-by-token for better UX
- Secure and production-aligned architecture
- Resume and interview-ready GenAI project

## 📈 Possible Enhancements

- 📌 Show source citations (page numbers)
- 🧠 Add conversational memory
- 📤 Upload PDFs dynamically
- 🌍 Deploy on Streamlit Cloud / Hugging Face Spaces
- 🔎 Add hybrid search (BM25 + vectors)

## 🎯 Use Cases

- Research paper Q&A
- Internal knowledge base chatbot
- Legal / policy document assistant
- Academic & technical document analysis

## 👨‍💻 Author
Tayyab Khan
<br>BTech in AI & Data Science<br>
Aspiring GenAI / AI Engineer

## ⭐ Final Note

This project demonstrates real-world GenAI engineering skills, including:

- RAG architecture
- Vector databases
- LLM orchestration
- Secure API handling
- Streaming UI

**If you find this useful, feel free to ⭐ star the repository!**
