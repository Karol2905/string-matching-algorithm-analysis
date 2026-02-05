def boyer_moore_search(text, pattern):
    """
    Boyer-Moore string matching algorithm (Bad Character Heuristic).

    Time Complexity:
    - Best case: sublinear in practice
    - Average case: O(n / m)
    - Worst case: O(n * m)

    Where:
    n = length of the text
    m = length of the pattern
    """

    n = len(text)
    m = len(pattern)

    if m == 0 or m > n:
        return []

    # Build bad character table
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i

    matches = []
    shift = 0

    while shift <= n - m:
        j = m - 1

        # Compare from right to left
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            matches.append(shift)
            shift += m - bad_char.get(text[shift + m], -1) if shift + m < n else 1
        else:
            shift += max(1, j - bad_char.get(text[shift + j], -1))

    return matches
