# Task

# You are given two integer arrays,A and B  of dimensions NXM.
# Your task is to perform the following operations:

# Add (A + B)
# Subtract ( A-B )
# Multiply ( A*B )
# Integer Division (A /B )
# Mod ( A%B )
# Power (A ** B)
# Note
# There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.
# # ===================== Solution =====================
import numpy

n, m = map(int, input().split())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

b = []
for _ in range(n):
    b.append(list(map(int, input().split())))

A = numpy.array(a)
B = numpy.array(b)

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
