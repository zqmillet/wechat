from utilities.friend import Friend

def test_friend(core):
    for item in core.get_friends():
        friend = Friend(**item)

        print(repr(friend))
