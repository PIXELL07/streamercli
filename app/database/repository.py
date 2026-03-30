from app.database.db import SessionLocal
from app.database.models import Message

def save_message(user, room, content):
    db = SessionLocal()

    msg = Message(user=user, room=room, content=content)
    db.add(msg)
    db.commit()

    db.close()


def get_messages(room):
    db = SessionLocal()

    msgs = db.query(Message)\
             .filter(Message.room == room)\
             .order_by(Message.id.desc())\
             .limit(10)\
             .all()

    db.close()

    return list(reversed(msgs))