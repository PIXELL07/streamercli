from app.services.message_service import save_message

async def broadcast_message(room, data):
    save_message(room, data)
    await redis_client.publish(f"room:{room}", json.dumps(data))