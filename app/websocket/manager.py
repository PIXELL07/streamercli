class ConnectionManager:

    def __init__(self):
        self.connections = {}
        self.rooms = {}

    async def connect(self, user, websocket):
        await websocket.accept()
        self.connections[user] = websocket

    def disconnect(self, user):
        self.connections.pop(user, None)
        for room in self.rooms:
            self.rooms[room].discard(user)

    def join_room(self, user, room):
        if room not in self.rooms:
            self.rooms[room] = set()
        self.rooms[room].add(user)

    def get_users(self, room):
        return self.rooms.get(room, set())

    async def send(self, user, message):
        ws = self.connections.get(user)
        if ws:
            await ws.send_text(message)