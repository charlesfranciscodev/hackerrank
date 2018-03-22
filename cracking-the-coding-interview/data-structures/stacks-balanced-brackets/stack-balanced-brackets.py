def is_matched(expression):
    pairs = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in expression:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values():
            if (len(stack) == 0):
                return False
            top_char = stack.pop()
            if pairs[top_char] != char:
                return False
    return len(stack) == 0

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
