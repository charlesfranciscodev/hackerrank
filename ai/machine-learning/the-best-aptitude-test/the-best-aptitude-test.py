import numpy
import pandas

# https://www.datascience.com/blog/introduction-to-correlation-learn-data-science-tutorials
nb_test_cases = int(input())
for _ in range(nb_test_cases):
    nb_students = int(input())
    array = numpy.array([input().split() for _ in range(6)], float)
    dataframe = pandas.DataFrame(array.T)
    # Kendall Tau correlation coefficient
    best_test = dataframe.corr("kendall")[0][1:].idxmax()
    print(best_test)
