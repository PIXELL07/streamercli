# Fixed:
# get_message_history doesn't exist — the correct function name is get_messages
# from repository.py, wrapped via message_service. Added the wrapper function.

from app.services.message_service import save_message_service, get_message_history

def test_message_storage():
    save_message_service("alice", "general", "hello")
    messages = get_message_history("general")
    assert len(messages) > 0
