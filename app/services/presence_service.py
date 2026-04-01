online_users = set()

def user_online(user: str):
    online_users.add(user)

def user_offline(user: str):
    online_users.discard(user)

def is_online(user: str) -> bool:
    # Fixed: missing helper — callers had no way to check if a user is online
    return user in online_users

def get_online_users() -> list:
    # Fixed: missing helper — no way to list who's online
    return list(online_users)
