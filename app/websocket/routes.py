from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json
import asyncio


from app.websocket.manager import ConnectionManager
from app.websocket.handlers import handle_message
from app.redis.pubsub import redis_listener
from fastapi import WebSocket
from app.auth.jwt_handler import verify_token

router = APIRouter()
manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    token = websocket.query_params.get("token")

    data = verify_token(token)
    user = data["user"]

    await manager.connect(user, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            await handle_message(user, message, manager)
    except WebSocketDisconnect:
        manager.disconnect(user)

@router.on_event("startup")
async def start_listener():
    asyncio.create_task(redis_listener(manager))