import math

# Reference: https://tinyurl.com/y9mrq7dr
# y = mx + b

X = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
Y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

n = len(X)
sum_x = sum(X)
sum_y = sum(Y)
sum_x2 = sum(i * i for i in X)
sum_xy = sum(i * j for i, j in zip(X, Y))

b = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x ** 2)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)

print(round(m, 3))
