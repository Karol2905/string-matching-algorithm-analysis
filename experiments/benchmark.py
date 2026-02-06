import sys
import os
import time
import random
import string
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algorithms.rabin_karp import rabin_karp_search
from algorithms.kmp import kmp_search
from algorithms.boyer_moore import boyer_moore_search
from algorithms.finite_automaton import finite_automaton_search
from algorithms.suffix_automaton import SuffixAutomaton


def generate_text(size):
    return ''.join(random.choices(string.ascii_lowercase, k=size))


def benchmark_all():
    pattern = "abcde"
    sizes = [1_000, 5_000, 10_000, 50_000, 100_000]
    runs = 5

    results = []

    for size in sizes:
        for _ in range(runs):
            text = generate_text(size)

            # Rabin-Karp
            start = time.perf_counter()
            rabin_karp_search(text, pattern)
            results.append(("Rabin-Karp", size, time.perf_counter() - start))

            # KMP
            start = time.perf_counter()
            kmp_search(text, pattern)
            results.append(("KMP", size, time.perf_counter() - start))

            # Boyer-Moore
            start = time.perf_counter()
            boyer_moore_search(text, pattern)
            results.append(("Boyer-Moore", size, time.perf_counter() - start))

            # Finite Automaton
            start = time.perf_counter()
            finite_automaton_search(text, pattern)
            results.append(("Finite Automaton", size, time.perf_counter() - start))

            # Suffix Automaton (build once per text)
            sa = SuffixAutomaton(text)
            start = time.perf_counter()
            sa.search(pattern)
            results.append(("Suffix Automaton", size, time.perf_counter() - start))

    df = pd.DataFrame(results, columns=["algorithm", "text_size", "time"])
    df = df.groupby(["algorithm", "text_size"]).mean().reset_index()
    return df


if __name__ == "__main__":
    df = benchmark_all()
    print(df)
    df.to_csv("experiments/all_algorithms_results.csv", index=False)
