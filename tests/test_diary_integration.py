from lib.diary import Diary
from lib.diary_entry import DiaryEntry

# DIARY TESTS #

def test_diary_add():
    new_diary_entry = DiaryEntry('Entry1', 'Contents1')
    new_diary = Diary()
    new_diary.add(new_diary_entry)
    assert new_diary.contents == { 'Entry1' : 'Contents1' }

def test_diary_all():
    new_diary_entry1 = DiaryEntry('Entry1', 'Contents1')
    new_diary_entry2 = DiaryEntry('Entry2', 'Contents2')
    new_diary = Diary()
    new_diary.add(new_diary_entry1)
    new_diary.add(new_diary_entry2)
    result = new_diary.all()
    assert result == { 'Entry1' : 'Contents1', 'Entry2' : 'Contents2' }

def test_count_words_low(self):
    new_diary_entry1 = DiaryEntry('Entry1', 'Contents1')
    new_diary_entry2 = DiaryEntry('Entry2', 'Contents2')
    new_diary = Diary()
    new_diary.add(new_diary_entry1)
    new_diary.add(new_diary_entry2)
    result = new_diary.count_words()
    assert result == 2

def test_count_words_low():
    new_diary_entry1 = DiaryEntry('Entry1', 'Contents1 Contents1 Contents1')
    new_diary_entry2 = DiaryEntry('Entry2', 'Contents2 Contents2 Contents2')
    new_diary = Diary()
    new_diary.add(new_diary_entry1)
    new_diary.add(new_diary_entry2)
    result = new_diary.count_words()
    assert result == 6

def test_reading_time_low():
    new_diary_entry1 = DiaryEntry('Entry1', 'Contents1 Contents1 Contents1')
    new_diary_entry2 = DiaryEntry('Entry2', 'Contents2 Contents2 Contents2')
    new_diary = Diary()
    new_diary.add(new_diary_entry1)
    new_diary.add(new_diary_entry2)
    result = new_diary.reading_time(6)
    assert result == 1

def test_reading_time_high():
    new_diary_entry1 = DiaryEntry('Entry1', 'Contents1 Contents1 Contents1')
    new_diary_entry2 = DiaryEntry('Entry2', 'Contents2 Contents2')
    new_diary = Diary()
    new_diary.add(new_diary_entry1)
    new_diary.add(new_diary_entry2)
    result = new_diary.reading_time(1)
    assert result == 5

def test_reading_time_roundup():
    new_diary_entry1 = DiaryEntry('Entry1', 'Contents1 Contents1 Contents1')
    new_diary_entry2 = DiaryEntry('Entry2', 'Contents2 Contents2')
    new_diary = Diary()
    new_diary.add(new_diary_entry1)
    new_diary.add(new_diary_entry2)
    result = new_diary.reading_time(10)
    assert result == 1

def test_reading_time_fraction():
    new_diary_entry1 = DiaryEntry('Entry1', 'Contents1 Contents1 Contents1')
    new_diary_entry2 = DiaryEntry('Entry2', 'Contents2 Contents2')
    new_diary = Diary()
    new_diary.add(new_diary_entry1)
    new_diary.add(new_diary_entry2)
    result = new_diary.reading_time(2)
    assert result == 3

def test_find_best_entry_for_reading_time_low():
    new_diary_entry1 = DiaryEntry('Entry1', 'Contents1 Contents1 Contents1')
    new_diary_entry2 = DiaryEntry('Entry2', 'Contents2')
    new_diary = Diary()
    new_diary.add(new_diary_entry1)
    new_diary.add(new_diary_entry2)
    result = new_diary.find_best_entry_for_reading_time(2, 1):
    assert result == {'Entry1': 'Contents1 Contents1 Contents1'}

def test_find_best_entry_for_reading_time_exact():
    new_diary_entry1 = DiaryEntry('Entry1', 'Contents1 Contents1 Contents1')
    new_diary_entry2 = DiaryEntry('Entry2', 'Contents2 Contents2 Contents2 Contents2')
    new_diary = Diary()
    new_diary.add(new_diary_entry1)
    new_diary.add(new_diary_entry2)
    result = new_diary.find_best_entry_for_reading_time(2, 2):
    assert result == {'Entry2': 'Contents1 Contents1 Contents1'}
