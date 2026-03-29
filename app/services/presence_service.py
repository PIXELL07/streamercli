online_users = set()

def user_online(user):
    online_users.add(user)

def user_offline(user):
    online_users.discard(user)