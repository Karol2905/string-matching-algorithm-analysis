# Experimental Analysis of String Matching Algorithms

## 1. Introduction and General Context

String matching is a fundamental problem in computer science that consists of finding the occurrence of a pattern within a larger text.  
This problem appears in many real-world applications such as search engines, text editors, bioinformatics, plagiarism detection, and network security.

Numerous algorithms have been developed to solve this problem, each using different strategies and offering different performance guarantees.  
Although many of these algorithms share similar theoretical time complexities, their practical behavior may vary significantly due to preprocessing costs, constant factors, and memory usage.

The objective of this project is to experimentally analyze and compare several string matching algorithms, observing how they behave in practice as the input size increases.

---

## 2. Algorithms Analyzed

The following five algorithms were implemented and analyzed in this project:

### Rabin–Karp
A hashing-based algorithm that uses a rolling hash function to compare the pattern with substrings of the text.

### Knuth–Morris–Pratt (KMP)
An algorithm that avoids redundant comparisons by using a prefix table (LPS), guaranteeing linear-time performance in the worst case.

### Boyer–Moore
An algorithm that compares the pattern from right to left and applies heuristic rules to skip large portions of the text.

### Finite Automaton String Matching
An algorithm that builds a deterministic finite automaton from the pattern, allowing linear-time scanning of the text.

### Suffix Automaton
An automaton that represents all substrings of the text and enables very fast pattern existence queries.

All algorithms address the same general problem of single-pattern string matching, although they rely on conceptually different approaches.

---

## 3. Experimental Methodology

### 3.1 Implementation

All algorithms were implemented from scratch in Python, without using built-in string search functions.  
Each implementation includes comments describing its logic and theoretical time complexity (Big-O).

A comprehensive set of unit tests was developed for each algorithm to ensure correctness across different scenarios, including edge cases.

---

### 3.2 Data Generation

For the experimental evaluation:

- Input texts were randomly generated using lowercase alphabetic characters.
- A fixed pattern was used across all experiments.
- Multiple input sizes were tested to analyze scalability.

The range of text sizes evaluated was:

- **1,000**
- **5,000**
- **10,000**
- **50,000**
- **100,000** characters

To reduce measurement noise:

- Each experiment was executed multiple times.
- The **average execution time** was computed for each input size.

---

### 3.3 Measurement and Visualization

Execution time was measured using high-resolution timers.  
The collected results were stored and visualized through graphs that show the relationship between:

- Input text size
- Average execution time

Both individual performance graphs and a final comparative graph were generated.

---

## 4. Results and Analysis

The experimental results reveal clear differences in the practical behavior of the analyzed algorithms:

- **Suffix Automaton** achieved the fastest search times, with execution time remaining almost constant as the text size increased.  
  This is because, after preprocessing, pattern searching depends only on the pattern length.  
  However, this algorithm only determines whether a pattern exists in the text and does not return the positions of occurrences.

- **Boyer–Moore** demonstrated the best practical performance among the algorithms that return match positions.  
  Its ability to skip large portions of the text explains its superior performance in typical cases.

- **KMP** and **Finite Automaton** exhibited stable and predictable linear behavior.  
  Both guarantee linear-time performance, although preprocessing introduces a slight overhead compared to Boyer–Moore.

- **Rabin–Karp** was the slowest algorithm in this experiment.  
  Despite acceptable average performance, hashing overhead and the lack of large jumps in the text negatively affect its practical efficiency.

## 5. Conclusions

This project demonstrates that theoretical time complexity alone is not sufficient to predict real-world performance.  
Factors such as preprocessing cost, hidden constants, memory usage, and the type of output produced play a critical role in practical algorithm selection.

In summary:

- **Fastest search:** Suffix Automaton (search phase only)
- **Best practical performance with match positions:** Boyer–Moore
- **Most stable and predictable:** KMP and Finite Automaton
- **Slowest in practice:** Rabin–Karp

The choice of a string matching algorithm depends on application requirements, including performance guarantees, memory constraints, and the type of results needed.
