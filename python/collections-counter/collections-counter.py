from collections import Counter

nb_shoes = int(input())
counter = Counter(list(map(int, input().split())))
nb_customers = int(input())
earnings = 0
for _ in range(nb_customers):
    size, price = map(int, input().split())
    if (counter.get(size, 0) != 0):
        counter[size] -= 1
        earnings += price
print(earnings)
