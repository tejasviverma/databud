import os 
import pandas as pd

from app.services.analyzer import analyze_dataframe
from fastapi import FastAPI, UploadFile, File

app = FastAPI(title="DataBud AI Analyst")


@app.get("/")
def root():
    return {
        "message": "Welcome to DataBud AI Analyst"
    }

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):

    file_path = os.path.join("uploads", file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    df = pd.read_csv(file_path)

    analysis = analyze_dataframe(df)

    return {
        "filename": file.filename,
        "analysis": analysis
    }