from algorithms.rabin_karp import rabin_karp_search


def test_basic_match():
    assert rabin_karp_search("ababcabcab", "abc") == [2, 5]


def test_no_match():
    assert rabin_karp_search("abcdef", "gh") == []


def test_single_character():
    assert rabin_karp_search("aaaaa", "a") == [0, 1, 2, 3, 4]


def test_pattern_equals_text():
    assert rabin_karp_search("hello", "hello") == [0]


def test_empty_pattern():
    assert rabin_karp_search("hello", "") == []


def test_pattern_longer_than_text():
    assert rabin_karp_search("hi", "hello") == []
