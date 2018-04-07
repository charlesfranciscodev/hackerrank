import numpy

numpy.set_printoptions(sign=' ')
a = numpy.array(list(map(float, input().split())))
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
