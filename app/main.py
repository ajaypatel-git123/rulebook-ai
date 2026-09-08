from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.reasoner import classify_question


app = FastAPI(title="Rulebook AI")


app.mount("/static", StaticFiles(directory="static"), name="static")


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/ask")
def ask_question(request: QuestionRequest):
    return classify_question(request.question)