from lib.diary_entry import DiaryEntry

# DIARY ENTRY TESTS #
test_string = 'A string to be tested'

def test_count_words():
    new_diary_entry = DiaryEntry('', 'Octopus Cat Dog Lizard Chimp')
    result = new_diary_entry.count_words()
    assert result == 5

def test_count_words_empty():
    new_diary_entry = DiaryEntry('', '')
    result = new_diary_entry.count_words()
    assert result == 0

def test_reading_time_low():
    new_diary_entry = DiaryEntry('', test_string)
    result = new_diary_entry.reading_time(200)
    assert result == 1

def test_reading_time_high():
    new_diary_entry = DiaryEntry('', 'A r e a l l y l o n g s t r i n g t h a t t a k e s o v e r a m i n u t e t o r A r e a l l y l o n g s t r i n g t h a t t a k e s o v e r a m i n u t e t o r A r e a l l y l o n g s t r i n g t h a t t a k e s o v e r a m i n u t e t o r')
    result = new_diary_entry.reading_time(50)
    assert result == 3

def test_reading_chunk_short():
    new_diary_entry = DiaryEntry('', test_string)
    result = new_diary_entry.reading_chunk(2, 1)
    assert result == 'A '

def test_reading_chunk_long():
    new_diary_entry = DiaryEntry('', test_string)
    result = new_diary_entry.reading_chunk(2, 5)
    assert result == 'A string t'