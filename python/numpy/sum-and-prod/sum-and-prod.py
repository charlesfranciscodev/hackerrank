import numpy

rows = []
n, m = map(int, input().split())
for _ in range(n):
    rows.append(list(map(int, input().split())))

a = numpy.array(rows, int)
print(numpy.prod(numpy.sum(a, axis=0)))
