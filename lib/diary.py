# File: lib/diary.py
from lib.diary_entry import DiaryEntry
import math

class Diary:
    def __init__(self):
        self.contents = {}

    def add(self, entry):
        self.contents[entry.title] = entry.contents

    def all(self):
        return self.contents

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        all_keys = self.contents.keys()
        all_values = self.contents.values()
        all_words = f'{" ".join(all_keys)} {" ".join(all_values)}'
        result = all_words.split()
        return len(result)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        total_words = self.count_words()
        return math.ceil(total_words / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass

new_diary_entry1 = DiaryEntry('Entry1', 'Contents1')
new_diary_entry2 = DiaryEntry('Entry2', 'Contents2')
new_diary_entry3 = DiaryEntry('Entry3', 'Contents3')
new_diary = Diary()
new_diary.add(new_diary_entry1)
new_diary.add(new_diary_entry2)
new_diary.add(new_diary_entry3)
print(new_diary.reading_time(2))