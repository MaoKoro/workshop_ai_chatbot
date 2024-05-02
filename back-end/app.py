from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from api_openai import chat_with_llm
from schemas import queryAI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to ChatBot API"}

@app.post("/conversation")
async def root(request: queryAI):
    return StreamingResponse(
        content=chat_with_llm(
            query=request.query,
            messages=request.messages,
            system=request.system
        ),
        media_type="text/event-stream"
    )