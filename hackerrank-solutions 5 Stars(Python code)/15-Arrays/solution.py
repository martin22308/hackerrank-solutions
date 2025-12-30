# The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.

# To use the NumPy module, we need to import it using:
#     import numpy
# Arrays
# A NumPy array is a grid of values. They are similar to lists, except that every element of an array must be the same type.
# ask

# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with the element type float.
# Input Format
# A single line of input containing space separated numbers.

# Output Format
# Print the reverse NumPy array with type float.
# ===================== Solution =====================
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr, float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)