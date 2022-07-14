from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)


@app.get("/")
def server_is_running():
    return {
        "message": "server is running"
    }


@app.get("/current_time")
def current_time():
    time_now = datetime.now().strftime("%H:%M")
    return {
        "current_time": time_now
    }

