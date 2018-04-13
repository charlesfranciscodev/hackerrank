if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max_score = -100
    runner_up = max_score
    for x in arr:
        if (x > max_score):
            runner_up = max_score
            max_score = x
        elif (x > runner_up and x != max_score):
            runner_up = x
    print(runner_up)
