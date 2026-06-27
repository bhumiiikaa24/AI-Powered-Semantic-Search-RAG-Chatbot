# AI-Powered Semantic Search RAG Chatbot

An AI-powered semantic search chatbot built using LangChain, Google Gemini API, Hugging Face embeddings, and ChromaDB.

## Features
- PDF document loading
- Text chunking and preprocessing
- Semantic search using vector embeddings
- Retrieval-Augmented Generation (RAG)
- Question-answering using Google Gemini
- Context-aware responses

## Tech Stack
- Python
- LangChain
- Google Gemini API
- Hugging Face Embeddings
- ChromaDB
- Sentence Transformers

## Project Structure
├── app.py
├── requirements.txt
├── src/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── rag.py

## Example Queries
- What skills are mentioned in the resume?
- Summarize the resume in 5 points.
- What projects has the candidate worked on?

## Future Improvements
- Streamlit frontend
- Multi-PDF support
- Chat history memory
- Document upload interface
