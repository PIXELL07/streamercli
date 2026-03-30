from app.websocket.manager import ConnectionManager

def test_join_room():

    manager = ConnectionManager()

    manager.join_room("alice", "general")
    manager.join_room("bob", "general")

    users = manager.get_users("general")

    assert "alice" in users
    assert "bob" in users


def test_leave_on_disconnect():

    manager = ConnectionManager()

    manager.join_room("alice", "general")
    manager.disconnect("alice")

    users = manager.get_users("general")

    assert "alice" not in users