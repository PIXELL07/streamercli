users = {}

def register(user, password):
    users[user] = password
    return True

def login(user, password):
    return users.get(user) == password