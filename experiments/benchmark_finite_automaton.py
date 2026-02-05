import sys
import os
import time
import random
import string
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algorithms.finite_automaton import finite_automaton_search


def generate_text(size):
    return ''.join(random.choices(string.ascii_lowercase, k=size))


def benchmark_finite_automaton():
    pattern = "abcde"
    sizes = [1_000, 5_000, 10_000, 50_000, 100_000]
    runs = 5

    results = []

    for size in sizes:
        total_time = 0.0
        for _ in range(runs):
            text = generate_text(size)

            start = time.perf_counter()
            finite_automaton_search(text, pattern)
            end = time.perf_counter()

            total_time += (end - start)

        avg_time = total_time / runs

        results.append({
            "algorithm": "Finite Automaton",
            "text_size": size,
            "avg_time_seconds": avg_time
        })

    return pd.DataFrame(results)


if __name__ == "__main__":
    df = benchmark_finite_automaton()
    print(df)
    df.to_csv("experiments/finite_automaton_results.csv", index=False)
