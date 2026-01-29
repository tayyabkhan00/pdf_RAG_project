import os

import streamlit as st

from langchain_community.vectorstores import FAISS
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

DB_PATH = "vectorstore"

# ----------------------------
# Load Vector Store (cached)
# ----------------------------
@st.cache_resource
def load_rag():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004"
    )

    vectorstore = FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = ChatGoogleGenerativeAI(
        model="models/gemini-flash-latest",
        temperature=0.2,
        streaming=True   # 🔥 ENABLE STREAMING
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an AI assistant.
Answer ONLY using the context below.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{question}
"""
    )

    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
    )

    return rag_chain


rag_chain = load_rag()

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="📄 PDF RAG Chatbot", layout="centered")

st.title("📄 PDF Q&A Chatbot")
st.caption("Powered by Gemini + LangChain + FAISS")

query = st.text_input("Ask a question from the PDF")

if query:
    with st.chat_message("user"):
        st.write(query)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""

        # 🔥 STREAMING RESPONSE
        for chunk in rag_chain.stream(query):
            if chunk.content:
                if isinstance(chunk.content, str):
                   full_response += chunk.content
                elif isinstance(chunk.content, list):
                    for item in chunk.content:
                        if isinstance(item, dict) and "text" in item:
                           full_response += item["text"]

                placeholder.markdown(full_response)

