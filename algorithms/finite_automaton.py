def build_transition_table(pattern, alphabet):
    """
    Build the DFA transition table for the given pattern.

    Time Complexity:
    - O(m * |Σ|)

    Where:
    m = length of the pattern
    |Σ| = size of the alphabet
    """
    m = len(pattern)
    delta = [{} for _ in range(m + 1)]

    for q in range(m + 1):
        for a in alphabet:
            k = min(m, q + 1)
            while k > 0 and not (pattern[:k] == (pattern[:q] + a)[-k:]):
                k -= 1
            delta[q][a] = k

    return delta


def finite_automaton_search(text, pattern, alphabet=None):
    """
    Finite Automaton string matching algorithm.

    Time Complexity:
    - Preprocessing: O(m * |Σ|)
    - Searching: O(n)
    - Total: O(n + m * |Σ|)

    Where:
    n = length of the text
    m = length of the pattern
    |Σ| = alphabet size
    """

    n = len(text)
    m = len(pattern)

    if m == 0 or m > n:
        return []

    # Define alphabet if not provided
    if alphabet is None:
        alphabet = set(text) | set(pattern)

    delta = build_transition_table(pattern, alphabet)

    state = 0
    matches = []

    for i, char in enumerate(text):
        state = delta[state].get(char, 0)
        if state == m:
            matches.append(i - m + 1)

    return matches
