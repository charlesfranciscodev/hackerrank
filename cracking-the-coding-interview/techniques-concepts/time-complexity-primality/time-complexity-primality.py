import math

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    print("Prime" if is_prime(n) else "Not prime")
