from fastapi import FastAPI
from pydantic import BaseModel

from app.rag import build_rag_chain

app = FastAPI(title="RAG API")

rag_chain = None


@app.on_event("startup")
def startup():
    global rag_chain
    rag_chain = build_rag_chain()


class Question(BaseModel):
    question: str


@app.post("/ask")
def ask(q: Question):
    answer = rag_chain.invoke(q.question)
    return {"question": q.question, "answer": answer}