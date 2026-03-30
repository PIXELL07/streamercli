from app.database.repository import save_message, get_messages

def save_message_service(user, room, message):
    save_message(user, room, message)

def get_message_history(room):
    return get_messages(room)