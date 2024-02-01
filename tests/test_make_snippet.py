from lib.make_snippet import *

def test_first_five_words():
    assert make_snippet("These are the first five") == "These are the first five"

def test_less_than_five():
    assert make_snippet("These are two") == "These are two"

def test_greater_than_five():
    assert make_snippet("These are more than five words") == ("These are more than five...")