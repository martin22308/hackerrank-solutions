# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.
# Input Format

# The first line contains the integer n, the number of students
# ' records. The next  n lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.
# Output Format

# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
# Input (stdin)
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# ===================== Solution =====================

n = int(input("n number of students:"))
students = {}
for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    students[name] = marks

query_name = input()

avg = sum(students[query_name]) / len(students[query_name])
print(f"{avg:.2f}")
