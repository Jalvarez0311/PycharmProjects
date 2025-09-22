from fastapi import FastAPI
from remote_api import router as remote_router

app = FastAPI()

app.include_router(remote_router, prefix="/remote")