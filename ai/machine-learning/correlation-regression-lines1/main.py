import math

# Reference http://www.statisticshowto.com/probability-and-statistics/correlation-coefficient-formula/
X = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
Y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
XY = [i * j for i, j in zip(X, Y)]
X2 = [i ** 2 for i in X]
Y2 = [j ** 2 for j in Y]
sum_X = sum(X)
sum_Y = sum(Y)
sum_XY = sum(XY)
sum_X2 = sum(X2)
sum_Y2 = sum(Y2)
n = len(X)
a = (n * sum_XY) - (sum_X * sum_Y)
b = math.sqrt(((n * sum_X2) - (sum_X ** 2)) * ((n * sum_Y2) - (sum_Y ** 2)))
coefficient = a / b
print(coefficient)
