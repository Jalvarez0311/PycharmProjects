from fastapi import APIRouter
from remote_tools import SystemStats
from fastapi import FastAPI

router = APIRouter()
system_stats = SystemStats()
app = FastAPI()

@app.get("/remote/mem")
def get_memory_usage():
    return {"memory_usage": 70}

@app.get("/remote/cpu")
def get_cpu_usage():
    return {"cpu_usage": 50}

@app.get("/remote/disk")
def get_disk_usage():
    return {"disk_usage": 60}
