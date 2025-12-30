# shape

# The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.
# Task

# You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.
# Input Format

# A single line of input containing 9 space separated integers.

# Output Format

# Print the 3X3 NumPy array.
# ===================== Solution =====================
import numpy

arr = list(map(int, input().split()))

result = numpy.array(arr).reshape(3, 3)

print(result)
