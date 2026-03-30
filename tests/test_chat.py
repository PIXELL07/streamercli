from app.services.message_service import save_message_service, get_message_history

def test_message_storage():

    save_message_service("alice", "general", "hello")

    messages = get_message_history("general")

    assert len(messages) > 0