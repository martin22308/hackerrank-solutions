# # Task

# # You are given a 2-D array with dimensions NXM.
# # Your task is to perform the sum tool over axis 0 and then find the product of that result.Input Format

# The first line of input contains space separated values of N  and M .
# The next N lines contains M space separated integers.

# Output Format

# Compute the sum along axis 0. Then, print the product of that sum.
# ===================== Solution =====================
import numpy

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

A = numpy.array(arr)

result = numpy.prod(numpy.sum(A, axis=0))

print(result)
