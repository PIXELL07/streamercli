def join_room(manager, user: str, room: str):
    manager.join_room(user, room)

def leave_room(manager, user: str, room: str):

    if room in manager.rooms:
        manager.rooms[room].discard(user)

def get_room_users(manager, room: str) -> list:
    return list(manager.get_users(room))
