import os
import shutil

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import pandas as pd

from app.agents.memory_agent import MemoryAgent
from app.services.analyzer import analyze_dataframe
from app.services.chat_analyst import answer_question
from app.agents.gemini_agent import GeminiAgent
from app.agents.query_agent import QueryAgent
from app.agents.router_agent import RouterAgent
from app.agents.document_agent import (
    DocumentAgent
)
from backend.app.agents.retriever_agent import RetrieverAgent


app = FastAPI()
memory_agent = MemoryAgent()




class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "Welcome to DataBud AI Analyst"
    }


@app.post("/upload")
async def upload_csv(
    file: UploadFile = File(...)
):


    df = pd.read_csv(file.file)

    analysis = analyze_dataframe(df)


    memory_agent.remember(
        "analysis",
        analysis
    )

    memory_agent.remember(
        "dataframe",
        df
    )

    return {
        "filename": file.filename,
        "analysis": analysis
    }


@app.post("/chat")
async def chat_with_data(
    request: QuestionRequest
):
    
    analysis = memory_agent.recall(
        "analysis"
    )

    df = memory_agent.recall(
        "dataframe"
    )

    if df is None or analysis is None:


        return {
            "error": "Please upload a CSV first."
        }

    chat_state = {
        "df": df,
        "question": request.question,
        "profile": analysis,
        "stats": analysis["numeric_summary"],
        "health_score": analysis["health_score"],
        "answer": None,
        "answered": False
    }

    router = RouterAgent()
    agent = router.run(chat_state)
    chat_state = agent.run(chat_state)

    if not chat_state["answered"]:

        gemini = GeminiAgent()

        chat_state = gemini.run(chat_state)

    return {
    "question": chat_state["question"],
    "answer": chat_state["answer"]
    }
    

@app.post("/upload-document")
async def upload_document(
    file: UploadFile = File(...)
):

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = os.path.join(
        "uploads",
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    state = {
        "file_path": file_path
    }

    document_agent = DocumentAgent()

    state = document_agent.run(state)

    memory_agent.remember(
        "knowledge",
        state["knowledge"]
    )

    memory_agent.remember(
        "vector_index",
        state["vector_index"]
    )

    return {
        "filename": file.filename,
        "characters": len(state["document_text"]),
        "chunks": len(state["knowledge"]) - 1,  # Subtracting 1 for the initial empty knowledge
        "preview": state["document_text"][:500]
    }

@app.post("/chat-document")
async def chat_document(
    request: QuestionRequest
):

    knowledge = memory_agent.recall(
        "knowledge"
    )

    vector_index = memory_agent.recall(
        "vector_index"
    )

    if knowledge is None or vector_index is None:

        return {
            "error": "Please upload a document first."
        }

    chat_state = {
        "question": request.question,
        "knowledge": knowledge,
        "vector_index": vector_index,
        "context": None,
        "answer": None
    }

    retriever_agent = RetrieverAgent()

    chat_state = retriever_agent.run(chat_state)

    gemini = GeminiAgent()

    chat_state = gemini.run(chat_state)

    return {
        "question": chat_state["question"],
        "context": chat_state["context"],
        "answer": chat_state["answer"]
    }