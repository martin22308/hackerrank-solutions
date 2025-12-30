# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
# Input Format

# The first line contains an integer,N , the number of students.
# The 2N subsequent lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.
# Output Format
# Print the name(s) of any student(s) having the second lowest grade in.
# If there are multiple students, order their names alphabetically and print each one on a new line.
# ===================== Solution =====================
students = []
n = int(input("n number of students:"))
for _ in range(n):
    name = input("Name :")
    grade = float(input("Grade :"))
    students.append([name, grade])

grades = sorted(set(student[1] for student in students))

second_lowest = grades[1]
names = [student[0] for student in students if student[1] == second_lowest]
for name in sorted(names):
    print(name)
