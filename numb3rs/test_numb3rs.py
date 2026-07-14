from numb3rs import validate

def test_right():
    assert validate("1.1.1.1") == True

def test_wrong():
    assert validate("256.1.1.1.1") == False
    assert validate("1.300.300.300") == False

