import json
from app.services.chat_service import broadcast_message
from app.services.moderation_service import is_muted
from app.services.rate_limit_service import check_rate

async def handle_message(user: str, data: dict, manager):

    # Fixed: check if user is muted before doing anything
    if is_muted(user):
        await manager.send(user, json.dumps({
            "type": "error",
            "message": "You are muted."
        }))
        return

    if not check_rate(user):
        await manager.send(user, json.dumps({
            "type": "error",
            "message": "You are sending messages too fast. Slow down."
        }))
        return

    msg_type = data.get("type", "message")

    # PRIVATE MESSAGE
    if msg_type == "private":
        to_user = data.get("to")
        message = data.get("message")

        if not to_user or not message:
            return  # Fixed: guard against malformed payloads

        payload = {
            "from": user,
            "message": message,
            "type": "private"
        }

        await manager.send(to_user, json.dumps(payload))
        return

    # NORMAL ROOM MESSAGE
    room = data.get("room", "general")
    message = data.get("message")

    if not message:
        return  

    manager.join_room(user, room)

    payload = {
        "user": user,
        "room": room,
        "message": message,
        "type": "message"
    }

    await broadcast_message(room, payload)
