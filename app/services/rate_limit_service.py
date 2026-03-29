limits = {}

def check_rate(user):
    limits[user] = limits.get(user, 0) + 1
    if limits[user] > 10:
        return False
    return True