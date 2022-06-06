from utilities.chatroom import Chatroom

def test_chatroom(core):
    for item in core.get_chatrooms():
        print(Chatroom(**item))
