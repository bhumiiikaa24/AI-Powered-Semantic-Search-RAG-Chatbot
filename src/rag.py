from langchain_google_genai import ChatGoogleGenerativeAI

def create_rag_chain(vector_store,api_key):
    llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=api_key,temperature=0.3)
    retriever=vector_store.as_retriever(search_kwargs={"k":3})
    return llm,retriever
    