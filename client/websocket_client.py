import asyncio
import websockets
import json

async def run():

    user = input("Username: ")
    uri = f"ws://localhost:8000/ws/{user}"

    async with websockets.connect(uri) as ws:

        async def send():
            while True:
                msg = input("> ")
                await ws.send(json.dumps({
                    "room": "general",
                    "message": msg
                }))

        async def receive():
            while True:
                print(await ws.recv())

        await asyncio.gather(send(), receive())

asyncio.run(run())