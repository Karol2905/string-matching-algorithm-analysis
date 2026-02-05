from algorithms.suffix_automaton import SuffixAutomaton


def test_pattern_exists():
    sa = SuffixAutomaton("ababcabcab")
    assert sa.search("abc") is True


def test_pattern_not_exists():
    sa = SuffixAutomaton("abcdef")
    assert sa.search("gh") is False


def test_single_character():
    sa = SuffixAutomaton("aaaaa")
    assert sa.search("a") is True


def test_pattern_equals_text():
    sa = SuffixAutomaton("hello")
    assert sa.search("hello") is True


def test_empty_pattern():
    sa = SuffixAutomaton("hello")
    assert sa.search("") is True
