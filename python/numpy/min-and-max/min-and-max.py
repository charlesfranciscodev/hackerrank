import numpy

n, m = map(int, input().split())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))
array = numpy.array(lines)
print(numpy.max(numpy.min(array, axis=1)))
