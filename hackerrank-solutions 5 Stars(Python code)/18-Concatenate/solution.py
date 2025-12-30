# Task

# You are given two integer arrays of size NXP and MXP ( N&M  are rows, and P is the column). Your task is to concatenate the arrays along axis 0.
# Input Format

# The first line contains space separated integers N,M  and P.
# The next N lines contains the space separated elements of the P columns.
# After that, the next M lines contains the space separated elements of the P columns.
# Output Format

# Print the concatenated array of size (N+M)XP.
# ===================== Solution =====================
import numpy

n, m, p = map(int, input().split())

arr1 = []
for _ in range(n):
    arr1.append(list(map(int, input().split())))

arr2 = []
for _ in range(m):
    arr2.append(list(map(int, input().split())))

a = numpy.array(arr1)
b = numpy.array(arr2)

print(numpy.concatenate((a, b), axis=0))
