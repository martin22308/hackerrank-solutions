# Task

# You are given two arrays A and B. Both have dimensions of NXM.
# Your task is to compute their matrix product.
# Input Format

# The first line contains the integer N.
# The next N lines contains N space separated integers of array A.
# # The following N lines contains N space separated integers of array B.
# Input (stdin)
# 2
# 1 2
# 3 4
# 1 2
# 3 4
# ===================== Solution =====================
import numpy

n = int(input())

A = numpy.array([list(map(int, input().split())) for _ in range(n)])
B = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(numpy.dot(A, B))
