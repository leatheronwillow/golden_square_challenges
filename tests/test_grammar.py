from lib.grammar import *

# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

"""
input: text,
output: string confirming that the first letter is capitalised.
        second part of string confirming that the sentence ends with proper punctuation.
        message saying the contrary if either of those things are not there.
"""

def test_output_is_string():
    assert type(grammar("")) == str

def test_empty_string():
    assert grammar("") == "text is empty"

def test_begins_with_capital():
    assert grammar("Hello World")[:23] == "first letter is capital"

def test_not_with_capital():
    assert grammar("hello World")[:27] == "first letter is not capital"

def test_punctuation_wrong():
    assert grammar("Hello World") == "first letter is capital but punctuation is incorrect"

def test_punctuation_correct():
    assert grammar("Hello World!") == "first letter is capital and punctuation is correct"

def test_punctuation_correct_alt():
    assert grammar("Hello World?") == "first letter is capital and punctuation is correct"