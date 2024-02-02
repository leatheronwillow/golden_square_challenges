from lib.diary_entry import *

class Diary():
    def __init__(self):
        self.entries = []
        pass

    def add(self, entry):
        self.entries.append(entry)
        return None
    
    def all(self):
        return self.entries
    
    def count_words(self):
        return sum([entry.count_words() for entry in self.entries])
    
    def reading_time(self, wpm):
        return math.ceil(self.count_words() / wpm)
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        max_words = wpm * minutes
        applicable_entries= [entry for entry in self.entries if entry.count_words() <= max_words]
        sorted_entries= sorted(applicable_entries, key=lambda entry: entry.count_words(), reverse=True)
        try:
            return sorted_entries[0]
        except IndexError:
            raise Exception("No entries can be read in that time")

    


    
    
