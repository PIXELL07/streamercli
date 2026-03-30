async def handle_message(manager, user, data):

    msg_type = data.get("type", "message")

    # PRIVATE MESSAGE
    if msg_type == "private":
        to_user = data.get("to")
        message = data.get("message")

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

    manager.join_room(user, room)

    payload = {
        "user": user,
        "room": room,
        "message": message,
        "type": "message"
    }

    await broadcast_message(room, payload)