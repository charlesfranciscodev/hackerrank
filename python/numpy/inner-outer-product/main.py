import numpy

a = numpy.array([input().split()], int)
b = numpy.array([input().split()], int)
print(numpy.inner(a, b)[0][0])
print(numpy.outer(a, b))
