from fastapi import FastAPI
from app.websocket.routes import router
from app.auth.auth_service import login, register

app = FastAPI()
app.include_router(router)


@app.post("/register")
def register_user(data: dict):
    return {"status": register(data["username"], data["password"])}


@app.post("/login")
def login_user(data: dict):
    token = login(data["username"], data["password"])
    return {"token": token}