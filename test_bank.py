from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("hello, Newman") == 0

def test_h():
    assert value("hi") == 20
    assert value("hey") == 20

def test_other():
    assert value("good morning") == 100

def test_case():
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("Hi") == 20
