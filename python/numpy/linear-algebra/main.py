import numpy as np

n = int(input())
a = np.array([input().split() for _ in range(n)], np.float)
print(round(np.linalg.det(a), 2))
