# 🤖 RAG Chatbot Project

An intelligent conversational system built with Retrieval-Augmented Generation (RAG). The system retrieves relevant information from uploaded documents and uses a Large Language Model (LLM) to generate accurate, document-grounded responses, reducing unsupported or irrelevant answers. The goal is to provide accurate, document-grounded responses while reducing unsupported or irrelevant answers.

## ✨ Key Features
- **Document Loading:** Supports PDF and TXT documents.
- **Text Processing:** Splits documents into smaller chunks with configurable overlap for better semantic search.
- **Vector Database:** Stores and retrieves document embeddings using ChromaDB to find the most relevant context.
- **LLM Integration:** Uses Groq API for fast and AI-powered response generation.
- **REST API:** Provides a robust API endpoint through FastAPI.
- **Chat Interface:** Offers an interactive chat UI built with Streamlit.
- **Context-Aware Responses:** Generates answers based strictly on the retrieved document content.

## 🛠️ Tech Stack
- **Python** & **LangChain**
- **FastAPI** (Backend API)
- **Streamlit** (Frontend UI)
- **Groq API** (LLM)
- **Hugging Face** (Embeddings)
- **ChromaDB** (Vector Database)

## 📂 Project Structure
    rag-ai-project/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── config.py
    │   ├── main.py
    │   ├── rag.py
    │   └── ui.py
    ├── docs/
    │   └── sample.txt
    ├── .env.example
    ├── .gitignore
    ├── requirements.txt
    └── README.md

## ⚙️ How it Works
1. Documents are loaded from the **docs** directory.
2. Text is split into smaller chunks.
3. Hugging Face creates embeddings for the chunks, which are stored in ChromaDB.
4. A retriever finds the most relevant document chunks for each question.
5. Groq generates a response using the retrieved context.
6. FastAPI handles requests, while Streamlit provides the user interface.

## 🚀 Setup & Configuration
Create a **.env** file in the project root and add your Groq API key:

    GROQ_API_KEY=your_api_key_here

*(Never commit your actual API key or other sensitive credentials to GitHub!)*

## 📡 API Endpoints
**Endpoint:** POST /ask

**Example Request:**

    {
      "question": "What is this document about?"
    }

**Example Response:**

    {
      "question": "What is this document about?",
      "answer": "The answer generated from the retrieved document context."
    }

## ⚙️ Configuration Options
The application includes configurable parameters (such as chunk size, overlap, and top-k retrieval) inside `app/config.py` for fine-tuning the RAG performance.
