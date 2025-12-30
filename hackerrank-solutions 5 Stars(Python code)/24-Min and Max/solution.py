# Task

# You are given a 2-D array with dimensions NXM.
# Your task is to perform the min function over axis 1 and then find the max of that.
# Input Format

# The first line of input contains the space separated values of N and M.
# The next  N lines contains M space separated integers.
# Output Format

# Compute the min along axis 1 and then print the max of that result.
# ===================== Solution =====================
import numpy

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

A = numpy.array(arr)

result = numpy.max(numpy.min(A, axis=1))

print(result)
