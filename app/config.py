import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "openai/gpt-oss-20b"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHROMA_PATH = "./chroma_db"
DOCS_PATH = "./docs"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
TOP_K = 3