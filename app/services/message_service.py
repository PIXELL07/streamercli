messages = {}

def save_message(room, data):

    if room not in messages:
        messages[room] = []

    messages[room].append(data)


def get_messages(room):
    return messages.get(room, [])[-10:]   # last 10 messages