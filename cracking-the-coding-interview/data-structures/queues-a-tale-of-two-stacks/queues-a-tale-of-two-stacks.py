class MyQueue(object):
    def __init__(self):
        self.stack_old = []
        self.stack_new = []

    def peek(self):
        self.update()
        return self.stack_old[-1]

    def pop(self):
        self.update()
        return self.stack_old.pop()

    def put(self, value):
        self.stack_new.append(value)

    def update(self):
        if (len(self.stack_old) == 0):
            while(len(self.stack_new) != 0):
                self.stack_old.append(self.stack_new.pop())


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
