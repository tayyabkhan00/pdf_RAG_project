from dotenv import load_dotenv
load_dotenv()

from langchain_community.vectorstores import FAISS
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

DB_PATH = "vectorstore"

def main():
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
        temperature=0.2
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

    # 🔥 LCEL-style RAG (NO deprecated chains)
    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
    )

    print("\n📄 PDF Q&A Bot (type 'exit' to quit)\n")

    while True:
        query = input("Ask a question: ")

        if query.lower() in ["exit", "quit"]:
            print("👋 Bye!")
            break

        response = rag_chain.invoke(query)
        answer = response.content

        if isinstance(answer, list):
            answer = answer[0]["text"]

        print("\nAnswer:\n", answer)

        print("-" * 60)

if __name__ == "__main__":
    main()
