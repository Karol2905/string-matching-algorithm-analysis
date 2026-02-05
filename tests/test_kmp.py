from algorithms.kmp import kmp_search


def test_basic_match():
    assert kmp_search("ababcabcab", "abc") == [2, 5]


def test_no_match():
    assert kmp_search("abcdef", "gh") == []


def test_single_character():
    assert kmp_search("aaaaa", "a") == [0, 1, 2, 3, 4]


def test_pattern_equals_text():
    assert kmp_search("hello", "hello") == [0]


def test_empty_pattern():
    assert kmp_search("hello", "") == []


def test_pattern_longer_than_text():
    assert kmp_search("hi", "hello") == []
