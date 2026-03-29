from fastapi import FastAPI
from app.websocket.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Chat server running"}