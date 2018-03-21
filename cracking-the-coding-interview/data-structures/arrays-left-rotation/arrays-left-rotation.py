n, rotations = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
for i in range(rotations, len(a)):
    print(a[i], end=' ')
for i in range(0, rotations - 1):
    print(a[i], end=' ')
print(a[rotations - 1], end='')
