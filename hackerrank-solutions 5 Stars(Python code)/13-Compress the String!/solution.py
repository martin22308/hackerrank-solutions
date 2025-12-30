# In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

# You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

# For a better understanding of the problem, check the explanation.

# Input Format

# A single line of input consisting of the string S.
# Output Format

# A single line of output consisting of the modified string.
# ===================== Solution =====================
from itertools import groupby

s = input().strip()

result = []
for key, group in groupby(s):
    result.append(f"({len(list(group))}, {key})")

print(" ".join(result))