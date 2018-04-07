import numpy

numpy.set_printoptions(sign=' ')

n, m = map(int, input().split())

# n X m Dimensional array with middle diagonal.
eye = numpy.eye(n, m)
identity = numpy.identity(n)
print(eye)  
