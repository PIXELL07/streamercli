from pydantic import BaseModel

class MessageSchema(BaseModel):
    user: str
    room: str
    message: str