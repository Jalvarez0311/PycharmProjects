from fastapi import FastAPI
from todo2 import todo_router
app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return { "message": "Hello World"}