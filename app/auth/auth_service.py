from app.auth.jwt_handler import create_token

users = {}

def register(user, password):
    users[user] = password
    return True

def login(user, password):
    if users.get(user) == password:
        return create_token(user)
    return None