from lib.diary_entry import *
from lib.diary import *
import pytest

def test_diary_add_entry():
    diary = Diary()
    entry1 = DiaryEntry("Today", "It was an okay day")
    entry2 = DiaryEntry("Yesterday", "Yesterday was much much worse. Bad stuff happened")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]

def test_diary_count_words():
    diary = Diary()
    entry1 = DiaryEntry("Today", "It was an okay day")
    entry2 = DiaryEntry("Yesterday", "Yesterday was much much worse. Bad stuff happened")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == 15
    entry3 = DiaryEntry("Tomorrow", "Tomorrow is bleak")
    diary.add(entry3)
    assert diary.count_words() == 19

def test_reading_time():
    diary = Diary()
    entry1 = DiaryEntry("Today", "It was an okay day")
    entry2 = DiaryEntry("Yesterday", "Yesterday was much much worse. Bad stuff happened")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.reading_time(1) == 15
    assert diary.reading_time(2) == 8
    assert diary.reading_time(5) == 3

def test_best_entry_for_reading_time():
    diary = Diary()
    entry1 = DiaryEntry("Today", "It was an okay day")
    entry2 = DiaryEntry("Yesterday", "Yesterday was much much worse. Bad stuff happened")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(1,6) == entry1
    assert diary.find_best_entry_for_reading_time(2,6) == entry2

def test_best_entry_for_reading_time():
    diary = Diary()
    entry1 = DiaryEntry("Today", "It was an okay day")
    diary.add(entry1)
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(1,3)
    assert str(e.value) == "No entries can be read in that time"