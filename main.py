from typing import final
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
    hours = int(time_now.split(":")[0]) -3 
    convert_time = f'{hours}:{time_now.split(":")[1]}'
    return {
        "current_time": convert_time
    }

