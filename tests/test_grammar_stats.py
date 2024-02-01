from lib.grammar_stats import *

def test_check():
    stats = GrammarStats()
    assert stats.check("Hello World!") == True
    assert stats.check("Hello World") == False
    assert stats.check("Hello World.") == True
    assert stats.check("hello World.") == False
    assert stats.check("Yellow World?") == True

def test_percentage_good():
    stats = GrammarStats()
    stats.check("Hello World!") == True
    stats.check("Hello World") == False
    stats.check("Hello World.") == True
    stats.check("hello World.") == False
    stats.check("Yellow World?") == True
    assert stats.percentage_good() == 60
    stats.check("Whats up duck?")
    assert stats.percentage_good() == 67




