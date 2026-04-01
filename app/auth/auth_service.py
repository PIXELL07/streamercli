from app.auth.jwt_handler import create_token
from app.auth.password import hash_password, verify_password

# Fixed: store hashed passwords, not plain text
users = {}


def register(user: str, password: str) -> bool:
    if user in users:
        return False  # Fixed
    users[user] = hash_password(password)
    return True


def login(user: str, password: str):
    hashed = users.get(user)
    if hashed and verify_password(password, hashed):
        return create_token(user)
    return None
