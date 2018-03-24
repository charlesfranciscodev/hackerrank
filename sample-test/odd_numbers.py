def oddNumbers(left, right):
    numbers = []
    if left % 2 == 0:
        left += 1
    if right % 2 == 1:
        right += 2
    for i in range(left, right, 2):
        numbers.append(i)
    return numbers
