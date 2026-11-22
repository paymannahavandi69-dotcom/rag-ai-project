from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from chromadb import PersistentClient
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

from app.config import (
    GROQ_MODEL,
    EMBEDDING_MODEL,
    CHROMA_PATH,
    DOCS_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K
)


def load_documents():
    docs = []
    for filename in os.listdir(DOCS_PATH):
        filepath = os.path.join(DOCS_PATH, filename)

        if filename.endswith(".txt"):
            loader = TextLoader(filepath, encoding="utf-8")
        elif filename.endswith(".pdf"):
            loader = PyPDFLoader(filepath)
        else:
            continue

        docs.extend(loader.load())
    return docs


def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(docs)


def build_rag_chain():
    docs = load_documents()
    chunks = split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    client = PersistentClient(path=CHROMA_PATH)
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        client=client
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": TOP_K})

    model = ChatGroq(model=GROQ_MODEL, temperature=0)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Answer only based on the text below. If the answer is not in the text, say 'I don't know'.\n\n{context}"),
        ("human", "{question}")
    ])

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )
    return chain