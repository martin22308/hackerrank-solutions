# Task

# You are given a 2-D array of size nXm.
# Your task is to find:

# 1-The mean along axis 1
# 2-The var along axis 0
# 3-The std along axis none
# Input (stdin)
# 2 2
# 1 2
# 3 4

# ===================== Solution =====================
import numpy

n, m = map(int, input().split())
A = numpy.array([list(map(float, input().split())) for _ in range(n)])

# Mean & Var (NumPy default output)
print(numpy.mean(A, axis=1))
print(numpy.var(A, axis=0))

# Std (special formatting)
std_val = numpy.std(A)

if std_val == 0:
    print("0.0")
else:
    print("{:.11f}".format(std_val))