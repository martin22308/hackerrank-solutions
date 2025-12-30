# Task
# You are given a string S.
# Your task is to print all possible size K replacement combinations of the string in lexicographic sorted order.
# Input Format

# A single line containing the string S and K integer value  separated by a space.

# Output Format

# Print the combinations with their replacements of string S on separate lines.
# ===================== Solution =====================
from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)

s = sorted(s)

for c in combinations_with_replacement(s, k):
    print("".join(c))
