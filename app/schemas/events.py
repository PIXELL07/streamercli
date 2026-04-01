from pydantic import BaseModel
from typing import Optional


class Event(BaseModel):
    # Fixed: was a plain class with a string constant — not a real schema.
    type: str
    room: Optional[str] = "general"
    message: Optional[str] = None
    to: Optional[str] = None  # for private messages
