from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

import pandas as pd

from app.services.analyzer import analyze_dataframe
from app.services.chat_analyst import answer_question

from app.agents.query_agent import (
    QueryAgent
)

app = FastAPI()

current_dataframe = None
current_analysis = None

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

    global current_dataframe

    df = pd.read_csv(file.file)

    current_dataframe = df

    analysis = analyze_dataframe(df)
    global current_analysis
    current_analysis = analysis

    return {
        "filename": file.filename,
        "analysis": analysis
    }

@app.post("/chat")
async def chat_with_data(
    request: QuestionRequest
):

    global current_dataframe
    global current_analysis

    if current_dataframe is None:

        return {
            "error":
            "Please upload a CSV first."
        }

    query_agent = QueryAgent()

    result = query_agent.run(
        request.question,
        {
            "profile": current_analysis,
            "stats": current_analysis["numeric_summary"],
            "health_score": current_analysis["health_score"]
        }
    )

    if result["answered"]:

        return {
            "question": request.question,
            "answer": result["answer"]
        }

    answer = answer_question(
        current_dataframe,
        request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }