import json
from app.services.chat_service import broadcast_message

async def handle_message(manager, user, data):
    room = data.get("room", "general")
    message = data.get("message")

    manager.join_room(user, room)

    payload = {
        "user": user,
        "room": room,
        "message": message
    }

    await broadcast_message(room, payload)