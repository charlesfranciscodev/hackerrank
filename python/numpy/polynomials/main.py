import numpy

polynomial = list(map(float, input().split()))
x = float(input())
print(numpy.polyval(polynomial, x))
