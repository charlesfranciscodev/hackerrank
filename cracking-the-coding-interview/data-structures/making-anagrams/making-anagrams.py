from functools import reduce

def number_needed(a, b):
    counter = [0] * 26
    for char in a:
        counter[ord(char) - ord('a')] += 1
    for char in b:
        counter[ord(char) - ord('a')] -= 1
    return reduce(lambda total, count: total + abs(count), counter, 0)

a = input().strip()
b = input().strip()
print(number_needed(a, b))
