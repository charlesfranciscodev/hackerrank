import numpy

n, m = map(int, input().split())
rows = []
for _ in range(n):
    row = list(map(int, input().split()))
    rows.append(row)
array = numpy.array(rows)
print(numpy.transpose(array))
print(array.flatten())
