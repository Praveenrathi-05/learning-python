from um import count

def test_single_um():
    assert count("um") == 1

def test_multiple_um():
    assert count("um um") == 2

def test_case_insensitive():
    assert count("Um uM UM") == 3

def test_punctuation():
    assert count("Um, thanks, um...") == 2

def test_not_inside_words():
    assert count("album yummy summary") == 0
