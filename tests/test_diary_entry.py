from lib.diary_entry import *

def test_format():
    entry = DiaryEntry("My Title", "These are the contents")
    assert entry.format() == "My Title: These are the contents"
    entry = DiaryEntry("Alternative Title", "Alternative content")
    assert entry.format() == "Alternative Title: Alternative content"

def test_count():
    entry = DiaryEntry("My Title", "These are the contents")
    assert entry.count_words() == 6
    entry = DiaryEntry("Alternative Title", "Alternative Content")
    assert entry.count_words() == 4

def test_reading_time():
    entry = DiaryEntry("Title", "Some contents here")
    assert entry.reading_time(2) == 2
    entry = DiaryEntry("Another title", "Some more contents here for funsies")
    assert entry.reading_time(3) == 3
    assert entry.reading_time(2) == 4

def test_reading_chunk():
    entry = DiaryEntry("Another Title", "Some contents here for funsies")
    assert entry.reading_chunk(2, 2) == "Another Title: Some contents"
    assert entry.reading_chunk(2, 1) == "here for"
    assert entry.reading_chunk(1, 2) == "funsies"
    assert entry.reading_chunk(1, 6) == "Another Title: Some contents here for"

def test_reading_chunk_end():
    entry = DiaryEntry("Another Title", "Some contents here for funsies")
    assert entry.reading_chunk(2, 2) == "Another Title: Some contents"
    assert entry.reading_chunk(2, 1) == "here for"
    assert entry.reading_chunk(1, 1) == "funsies"
    assert entry.reading_chunk(1, 1) == "Another"

