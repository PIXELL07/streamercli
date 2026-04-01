from app.database.repository import save_message, get_messages

def save_message_service(user: str, room: str, message: str):
    save_message(user, room, message)

def get_message_history(room: str):
    # Fix
    return get_messages(room)
