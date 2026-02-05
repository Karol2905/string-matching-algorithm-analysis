class State:
    def __init__(self):
        self.next = {}
        self.link = -1
        self.length = 0


class SuffixAutomaton:
    """
    Suffix Automaton for string matching.

    Time Complexity:
    - Construction: O(n)
    - Search: O(m)

    Where:
    n = length of the text
    m = length of the pattern
    """

    def __init__(self, text):
        self.states = [State()]
        self.last = 0

        for char in text:
            self._extend(char)

    def _extend(self, char):
        cur = len(self.states)
        self.states.append(State())
        self.states[cur].length = self.states[self.last].length + 1

        p = self.last
        while p >= 0 and char not in self.states[p].next:
            self.states[p].next[char] = cur
            p = self.states[p].link

        if p == -1:
            self.states[cur].link = 0
        else:
            q = self.states[p].next[char]
            if self.states[p].length + 1 == self.states[q].length:
                self.states[cur].link = q
            else:
                clone = len(self.states)
                self.states.append(State())
                self.states[clone].length = self.states[p].length + 1
                self.states[clone].next = self.states[q].next.copy()
                self.states[clone].link = self.states[q].link

                while p >= 0 and self.states[p].next.get(char) == q:
                    self.states[p].next[char] = clone
                    p = self.states[p].link

                self.states[q].link = self.states[cur].link = clone

        self.last = cur

    def search(self, pattern):
        """
        Search for a pattern in the text.

        Returns:
        True if the pattern exists, False otherwise.
        """
        state = 0
        for char in pattern:
            if char not in self.states[state].next:
                return False
            state = self.states[state].next[char]
        return True
