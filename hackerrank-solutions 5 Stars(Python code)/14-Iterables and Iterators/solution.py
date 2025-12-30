# The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

# To read more about the functions in this module, check out their documentation here.

# You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.

# Find the probability that at least one of the K indices selected will contain the letter: 'a'.

# Input Format
# The input consists of three lines. The first line contains the integer N, denoting the length of the list. The next line consists of  N space-separated lowercase English letters, denoting the elements of the list.
# The third and the last line of input contains the integer K, denoting the number of indices to be selected.

# Output Format
# Output a single line consisting of the probability that at least one of the K indices selected contains the letter:'a'.
# Note: The answer must be correct up to 3 decimal places.
# ===================== Solution =====================
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())
all_combinations = list(combinations(range(n), k))

count = 0
for comb in all_combinations:
    if any(letters[i] == 'a' for i in comb):
        count += 1

probability = count / len(all_combinations)

print(f"{probability:.3f}")