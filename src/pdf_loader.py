import os
from langchain_community.document_loaders import PyPDFLoader

def load_documents():
    documents=[]
    documents_path="documents"
    for filename in os.listdir(documents_path):
        if filename.endswith(".pdf"):
            pdf_path=os.path.join(documents_path,filename)
            loader=PyPDFLoader(pdf_path)
            pages=loader.load()
            documents.extend(pages)
    return documents