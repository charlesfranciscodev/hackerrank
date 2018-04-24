from collections import namedtuple

nb_students = int(input())
Student = namedtuple("Student", input())

total = 0
for _ in range(nb_students):
    row = input().split()
    student = Student(*row)
    total += int(student.MARKS)
average = total / nb_students 
print("{:.2f}".format(average))
