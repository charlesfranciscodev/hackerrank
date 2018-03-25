cache = {}

def nb_ways(x):
    if x == 1 or x == 2:
        return x
    if x == 3:
        return 4
    return cache[x - 1] + cache[x - 2] + cache[x - 3]

def fill_cache(n):
    for i in range(1, n):
        cache[i] = nb_ways(i)

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    cache.clear()
    fill_cache(n)
    print(nb_ways(n))
