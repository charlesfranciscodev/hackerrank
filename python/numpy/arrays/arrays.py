import numpy

def arrays(array):
    array = numpy.array(array, float)
    return(numpy.flip(array, 0))

print(arrays(input().split()))
