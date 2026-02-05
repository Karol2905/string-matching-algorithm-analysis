from algorithms.boyer_moore import boyer_moore_search


def test_basic_match():
    assert boyer_moore_search("ababcabcab", "abc") == [2, 5]


def test_no_match():
    assert boyer_moore_search("abcdef", "gh") == []


def test_single_character():
    assert boyer_moore_search("aaaaa", "a") == [0, 1, 2, 3, 4]


def test_pattern_equals_text():
    assert boyer_moore_search("hello", "hello") == [0]


def test_empty_pattern():
    assert boyer_moore_search("hello", "") == []


def test_pattern_longer_than_text():
    assert boyer_moore_search("hi", "hello") == []
