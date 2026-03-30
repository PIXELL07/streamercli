from fastapi.testclient import TestClient
from app.main import app
from app.auth.jwt_handler import create_token

client = TestClient(app)


def test_websocket_connection():

    token = create_token("alice")

    with client.websocket_connect(f"/ws?token={token}") as ws:
        ws.send_json({
            "type": "join",
            "room": "general"
        })

        ws.send_json({
            "type": "message",
            "room": "general",
            "message": "hello"
        })

        data = ws.receive_text()

        assert "hello" in data


def test_private_message():

    token1 = create_token("alice")
    token2 = create_token("bob")

    with client.websocket_connect(f"/ws?token={token1}") as ws1:
        with client.websocket_connect(f"/ws?token={token2}") as ws2:

            ws1.send_json({
                "type": "private",
                "to": "bob",
                "message": "hi bob"
            })

            data = ws2.receive_text()

            assert "hi bob" in data