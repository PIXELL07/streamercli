muted_users = set()

def mute(user: str):
    muted_users.add(user)

def unmute(user: str):
    # Fixed
    muted_users.discard(user)

def is_muted(user: str) -> bool:
    return user in muted_users
