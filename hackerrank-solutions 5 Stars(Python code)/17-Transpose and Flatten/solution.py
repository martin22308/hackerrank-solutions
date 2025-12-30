# Transpose

# We can generate the transposition of an array using the tool numpy.transpose.
# It will not affect the original array, but it will create a new array.
# Task

# You are given a NXM integer array matrix with space separated elements (N = rows and M = columns).
# Your task is to print the transpose and flatten results.

# Input Format

# The first line contains the space separated values of N and M.
# The next N lines contains the space separated elements of M columns.
# Output Format

# First, print the transpose array and then print the flatten.
# ===================== Solution =====================
import numpy
n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

arr = numpy.array(matrix)

print(numpy.transpose(arr))
print(arr.flatten())