from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json
import asyncio

from app.websocket.manager import ConnectionManager
from app.websocket.handlers import handle_message
from app.redis.pubsub import redis_listener

router = APIRouter()
manager = ConnectionManager()


@router.websocket("/ws/{user}")
async def websocket_endpoint(websocket: WebSocket, user: str):

    await manager.connect(user, websocket)

    try:
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)

            await handle_message(manager, user, data)

    except WebSocketDisconnect:
        manager.disconnect(user)


@router.on_event("startup")
async def start_listener():
    asyncio.create_task(redis_listener(manager))