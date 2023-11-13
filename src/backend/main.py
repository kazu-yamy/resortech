import socket

import uvicorn
from api import predict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict.router)


@app.get("/")
def demo():
    return {"response": "success"}


if __name__ == "__main__":
    ip = socket.gethostbyname(socket.gethostname())
    uvicorn.run(app, host=ip, port=8000, log_level="info")
