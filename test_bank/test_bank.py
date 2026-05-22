from bank import value

def test_default():
    assert value("world") == 100
def test_h():
    assert value("h world") == 20

def test_hello():
    assert value("hello world") == 0

def test_case():
     assert value("Hello world") == 0
