import json
import asyncio

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.websocket.manager import ConnectionManager
from app.websocket.handlers import handle_message
from app.redis.pubsub import redis_listener
from app.auth.jwt_handler import verify_token
from app.services.presence_service import user_online, user_offline

router = APIRouter()
manager = ConnectionManager()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    token = websocket.query_params.get("token")

    try:
        data = verify_token(token)
        user = data["user"]
    except Exception:
        await websocket.close(code=1008)
        return

    await manager.connect(user, websocket)
    user_online(user)  

    try:
        while True:
            raw = await websocket.receive_text()
            message = json.loads(raw)
            await handle_message(user, message, manager)
    except WebSocketDisconnect:
        manager.disconnect(user)
        user_offline(user)  

@router.on_event("startup")
async def start_listener():
    asyncio.create_task(redis_listener(manager))
