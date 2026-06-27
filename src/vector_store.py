from langchain_community.vectorstores import FAISS
from src.embeddings import create_embeddings

def create_vector_store(chunks):
    embeddings=create_embeddings()
    vector_store=FAISS.from_documents(documents=chunks,embedding=embeddings)
    return vector_store 