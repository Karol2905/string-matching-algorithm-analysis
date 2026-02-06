def kmp_search(text, pattern):
    """
    Knuth-Morris-Pratt (KMP) string matching algorithm.

    Time Complexity:
    - Preprocessing (LPS array): O(m)
    - Searching: O(n)
    - Total: O(n + m)

    Where:
    n = length of the text
    m = length of the pattern
    """

    n = len(text)
    m = len(pattern)

    if m == 0 or m > n:
        return []

    # Build LPS (Longest Prefix Suffix) array
    lps = [0] * m
    length = 0
    i = 1
    # lps[0]=0

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    # Search phase
    matches = []
    i = j = 0  # i -> text, j -> pattern

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches
