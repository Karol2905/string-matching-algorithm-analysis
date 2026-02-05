def rabin_karp_search(text, pattern, base=256, mod=101):
    """
    Rabin-Karp string matching algorithm.

    Time Complexity:
    - Best / Average case: O(n + m)
    - Worst case: O(n * m) due to hash collisions

    Where:
    n = length of the text
    m = length of the pattern
    """

    n = len(text)
    m = len(pattern)

    # Edge cases
    if m == 0 or m > n:
        return []

    matches = []

    # Hash values for pattern and current text window
    pattern_hash = 0
    window_hash = 0

    # h = base^(m-1) % mod, used to remove the leading character
    h = 1
    for _ in range(m - 1):
        h = (h * base) % mod

    # Compute initial hash for pattern and first window of text
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        window_hash = (base * window_hash + ord(text[i])) % mod

    # Slide the pattern over the text
    for i in range(n - m + 1):
        # If hash values match, verify characters one by one
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                matches.append(i)

        # Compute hash of the next window using rolling hash
        if i < n - m:
            window_hash = (
                base * (window_hash - ord(text[i]) * h)
                + ord(text[i + m])
            ) % mod

            # Ensure the hash value is positive
            if window_hash < 0:
                window_hash += mod

    return matches
