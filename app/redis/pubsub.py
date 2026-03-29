import json
from app.redis.redis_client import redis_client

async def redis_listener(manager):

    pubsub = redis_client.pubsub()
    await pubsub.psubscribe("room:*")

    async for message in pubsub.listen():

        if message["type"] != "pmessage":
            continue

        data = json.loads(message["data"])
        room = data["room"]

        users = manager.get_users(room)

        for user in users:
            await manager.send(user, json.dumps(data))