import monopoly


def setup():
    print("SETUP!")


def teardown():
    print("TEAR DOWN!")


def test_basic():
    print("I RAN!")


'''
TODO: Figure out how tests work
def test_modify_balance():
    game = monopoly()
    player = monopoly.Player(1, "Test", 1, M)
    player.modify_balance(1, M)
    assert player.get_balance() == 2000
'''
