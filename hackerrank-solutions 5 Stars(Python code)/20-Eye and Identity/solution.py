# Task

# Your task is to print an array of size NXM with its main diagonal elements as 1's and 0's everywhere else.
# put Format

# A single line containing the space separated values of N and M.
# N denotes the rows.
# M denotes the columns.
# Output Format
# Print the desired NXM array.
# ===================== Solution =====================
import numpy
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())

print(numpy.eye(n, m))