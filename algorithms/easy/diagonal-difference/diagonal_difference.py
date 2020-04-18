#!/bin/python3
import os


def diagonalDifference(arr):
    first_diagonal = 0
    for index in range(len(arr)):
        first_diagonal += arr[index][index]

    second_diagonal = 0
    for index in range(len(arr)):
        second_diagonal += arr[index][len(arr) - index - 1]

    return abs(first_diagonal - second_diagonal)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
