from lib.count_words import *

def test_returns_number():
    result = count_words("This is a string")
    assert isinstance(result, int) == True

def test_count_words():
    assert count_words("This is a string") == 4

def test_count_empty_string():
    assert count_words("") == 0
