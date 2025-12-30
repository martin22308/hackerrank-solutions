# Task
# You are given a 1-D array,A . Your task is to print the FLOOR, CEIL and RINT of all the elements of A.


# Input Format

# A single line of input containing the space separated elements of array A.

# ===================== Solution =====================
import numpy
numpy.set_printoptions(legacy='1.13')

arr = numpy.array(list(map(float, input().split())))

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
