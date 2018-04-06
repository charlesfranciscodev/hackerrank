import pandas
import numpy
from scipy import stats

sample_size = int(input())
array = numpy.array(list(map(int, input().split())))

mean = numpy.mean(array)
median = numpy.median(array)
mode = stats.mode(array)[0][0]
std = numpy.std(array)
ci = stats.norm.interval(0.950004, loc=mean, scale=std/numpy.sqrt(sample_size))

print("{0:.1f}".format(mean))
print("{0:.1f}".format(median))
print(mode)
print("{0:.1f}".format(std))
print("{0:.1f} {1:.1f}".format(ci[0], ci[1]))
