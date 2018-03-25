#!/bin/python3

import sys

def lonely_integer(a):
    visited = set()
    for i in a:
        if (i in visited):
            visited.remove(i)
        else:
            visited.add(i)
    return visited.pop()

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split()]
print(lonely_integer(a))
