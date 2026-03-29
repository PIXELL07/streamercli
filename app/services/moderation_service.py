muted_users = set()

def mute(user):
    muted_users.add(user)

def is_muted(user):
    return user in muted_users