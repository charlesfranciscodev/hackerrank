import numpy

rows1 = []
rows2 = []
n, m = map(int, input().split())
for _ in range(n):
    rows1.append(list(map(int, input().split())))
for _ in range(n):
    rows2.append(list(map(int, input().split())))

a = numpy.array(rows1, int)
b = numpy.array(rows2, int)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)
