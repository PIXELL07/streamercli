online = set()

def set_online(user):
    online.add(user)

def set_offline(user):
    online.discard(user)