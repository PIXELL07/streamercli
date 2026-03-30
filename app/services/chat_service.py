import json
from app.redis.redis_client import redis_client
from app.services.message_service import save_message_service

async def broadcast_message(room, data):

    save_message_service(
        data["user"],
        room,
        data["message"]
    )

    await redis_client.publish(f"room:{room}", json.dumps(data))