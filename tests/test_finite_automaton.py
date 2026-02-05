from algorithms.finite_automaton import finite_automaton_search


def test_basic_match():
    assert finite_automaton_search("ababcabcab", "abc") == [2, 5]


def test_no_match():
    assert finite_automaton_search("abcdef", "gh") == []


def test_single_character():
    assert finite_automaton_search("aaaaa", "a") == [0, 1, 2, 3, 4]


def test_pattern_equals_text():
    assert finite_automaton_search("hello", "hello") == [0]


def test_empty_pattern():
    assert finite_automaton_search("hello", "") == []


def test_pattern_longer_than_text():
    assert finite_automaton_search("hi", "hello") == []
