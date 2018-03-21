#!/bin/python3
import collections

def isValid(s):
    counter = collections.Counter(s)
    values = list(counter.values())
    values.sort()
    count_min = values.count(values[0])
    valid = count_min == len(values)
    valid_if_remove_max = count_min == len(values) - 1 and values[-1] - values[-2] == 1
    valid_if_remove_min = values.count(values[-1]) == len(values) -1 and values[0] == 1
    return valid or valid_if_remove_max or valid_if_remove_min

s = input().strip()

print("YES" if isValid(s) else "NO")
