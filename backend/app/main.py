from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import pandas as pd

from app.services.analyzer import analyze_dataframe
from app.services.chat_analyst import answer_question

from app.agents.query_agent import QueryAgent
from app.agents.router_agent import RouterAgent


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
    global current_analysis

    df = pd.read_csv(file.file)

    current_dataframe = df

    analysis = analyze_dataframe(df)

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
            "error": "Please upload a CSV first."
        }

    chat_state = {
        "df": current_dataframe,
        "question": request.question,
        "profile": current_analysis,
        "stats": current_analysis["numeric_summary"],
        "health_score": current_analysis["health_score"],
        "answer": None,
        "answered": False
    }

    router = RouterAgent()
    agent = router.run(chat_state)
    chat_state = agent.run(chat_state)
    return{
        "question": chat_state["question"],
        "answer": chat_state["answer"],
    }