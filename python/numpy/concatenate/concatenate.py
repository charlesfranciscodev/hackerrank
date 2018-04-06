import numpy

n, m, p = map(int, input().split())
rows1 = []
rows2 = []

for _ in range(n):
    row = list(map(int, input().split()))
    rows1.append(row)
for _ in range(m):
    row = list(map(int, input().split()))
    rows2.append(row)

array1 = numpy.array(rows1)
array2 = numpy.array(rows2)
print(numpy.concatenate((array1, array2), axis=0))
