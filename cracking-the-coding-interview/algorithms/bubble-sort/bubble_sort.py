n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swaps = 0

for i in range(0, n):
    for j in range(0, n - i - 1):
        # Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]):
            swaps += 1
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

print("Array is sorted in {} swaps.".format(swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
