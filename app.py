import os

from dotenv import load_dotenv

from src.pdf_loader import load_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.rag import create_rag_chain

def main():
    print("Program Started")
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    print(api_key[:10])
    print("Loading PDFs...")
    documents = load_documents()
    print(f"Loaded {len(documents)} pages")
    print("Splitting documents...")
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunks")
    print("Creating vector database...")
    vector_store = create_vector_store(chunks)
    print("Vector database ready!")
    llm, retriever = create_rag_chain(vector_store,api_key)

    while True:

        question = input("\nAsk a question (type exit to quit): ")

        if question.lower() == "exit":
            break

        docs = retriever.invoke(question)

        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
        Answer the question using the provided context.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

        response = llm.invoke(prompt)

        print("\nAnswer:")
        print(response.content)


if __name__ == "__main__":
    main()