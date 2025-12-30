# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.Input Format
# Input Format
# The first line contains n. The second line contains an array A[]  of  integers each separated by a space.
# Output Format

# Print the runner-up score.
# ===================== Solution =====================
n = int(input())
scores = list(map(int, input("inter space after num :").split()))

unique_scores = set(scores)

unique_scores.remove(max(unique_scores))
print(max(unique_scores))
