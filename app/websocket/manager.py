import json
class ConnectionManager:

    def __init__(self):
        self.connections = {}
        self.rooms = {}

    async def connect(self, user: str, websocket):
        await websocket.accept()
        self.connections[user] = websocket

    def disconnect(self, user: str):
        self.connections.pop(user, None)
        # Fixed: clean up user from all rooms on disconnect
        for room in list(self.rooms.keys()):
            self.rooms[room].discard(user)

    def join_room(self, user: str, room: str):
        if room not in self.rooms:
            self.rooms[room] = set()
        self.rooms[room].add(user)

    def get_users(self, room: str):
        return self.rooms.get(room, set())

    async def send(self, user: str, message: str):
        ws = self.connections.get(user)
        if ws:
            await ws.send_text(message)
