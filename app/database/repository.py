from app.database.db import SessionLocal
from app.database.models import Message


def save_message(user: str, room: str, content: str):
    db = SessionLocal()
    try:
        msg = Message(user=user, room=room, content=content)
        db.add(msg)
        db.commit()
    finally:
        db.close()  # Fixed: always close even if an error occurs


def get_messages(room: str):
    db = SessionLocal()
    try:
        msgs = db.query(Message)\
                 .filter(Message.room == room)\
                 .order_by(Message.id.desc())\
                 .limit(10)\
                 .all()
        return list(reversed(msgs))
    finally:
        db.close()  # Fixed
