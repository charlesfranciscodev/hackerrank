import math

n = int(input())
student_grades = [[input(), float(input())] for _ in range(n)]
students_second_lowest = []
min_grade = math.inf
second_lowest = min_grade

for student, grade in student_grades:
    if (grade < min_grade):
        second_lowest = min_grade
        min_grade = grade
    elif (grade < second_lowest and grade != min_grade):
        second_lowest = grade

for student, grade in student_grades:
    if (grade == second_lowest):
        students_second_lowest.append(student)

students_second_lowest.sort()
for student in students_second_lowest:
    print(student)
