Raj AI – Retrieval-Augmented Generation (RAG) Chatbot
Overview
Raj AI is an AI-powered Retrieval-Augmented Generation (RAG) application that allows users to ask questions about their own documents and receive context-aware answers.

The system retrieves relevant information from uploaded documents and uses a Large Language Model (LLM) to generate answers based on the retrieved content.

The goal is to provide accurate, document-grounded responses while reducing unsupported or irrelevant answers.

Key Features
Document Loading: Supports PDF and TXT documents.
Text Processing: Splits documents into smaller chunks with configurable overlap.
Semantic Search: Uses Hugging Face embeddings to find relevant information.
Vector Database: Stores and retrieves document embeddings using ChromaDB.
LLM Integration: Uses Groq API for AI-powered response generation.
REST API: Provides an API endpoint through FastAPI.
Chat Interface: Offers an interactive chatbot interface built with Streamlit.
Context-Aware Responses: Generates answers based on retrieved document content.
Tech Stack
Python
LangChain
FastAPI
Streamlit
Groq API
Hugging Face
ChromaDB
Sentence Transformers
Project Structure
raj-ai-project/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── rag.py
│   └── ui.py
│
├── docs/
│   └── sample.txt
│
├── .env.example
├── .gitignore
└── requirements.txt
How It Works
Documents are loaded from the docs directory.
Text is split into smaller chunks.
Hugging Face converts text chunks into embeddings.
ChromaDB stores the vector representations.
A retriever finds the most relevant document chunks for each question.
Groq generates a response using the retrieved context.
FastAPI handles requests, while Streamlit provides the user interface.
Configuration
Create a .env file in the project root and add your Groq API key:

GROQ_API_KEY=your_api_key_here
Never commit your actual API key or other sensitive credentials to GitHub.

API Endpoint
POST /ask

Example request:

{
  "question": "What is this document about?"
}
Example response:

{
  "question": "What is this document about?",
  "answer": "The answer generated from the retrieved document context."
}
Configuration Options
The application includes configurable parameters for:

LLM model
Embedding model
Document storage path
Vector database path
Chunk size
Chunk overlap
Number of retrieved documents
Future Improvements
Support for additional document formats.
Improved error handling.
Conversation memory.
Authentication and access control.
Cloud deployment and remote API access.
Developed by Raj AI Project

An AI-powered document question-answering system built with Python and modern AI technologies.
