from plates import is_valid

def test_valid():
    assert is_valid("CS50")
    assert is_valid("HELLO")
    assert is_valid("AAA222")

def test_length():
    assert not is_valid("A")
    assert not is_valid("ABCDEFG")

def test_first_two_letters():
    assert not is_valid("1A234")
    assert not is_valid("A1234")

def test_first_number_zero():
    assert not is_valid("CS05")
    assert not is_valid("AAA012")

def test_letters_after_numbers():
    assert not is_valid("CS50P")
    assert not is_valid("AA22BB")

def test_punctuation():
    assert not is_valid("PI3.14")
    assert not is_valid("CS 50")
