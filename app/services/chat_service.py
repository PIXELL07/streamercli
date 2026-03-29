import json
from app.redis.redis_client import redis_client

async def broadcast_message(room, data):
    await redis_client.publish(f"room:{room}", json.dumps(data))