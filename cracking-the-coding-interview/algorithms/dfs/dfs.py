from collections import deque


class Grid:
    def __init__(self):
        self.nodes = []
        self.visited = set()  # (x, y) points already visited

    def read_input(self):
        self.height = int(input().strip())
        self.width = int(input().strip())
        self.nodes = []
        for y in range(self.height):
            line = list(map(int, input().strip().split()))
            self.nodes.append(line)

    def get_biggest_region(self):
        max_area = 0
        for y1 in range(len(self.nodes)):
            line = self.nodes[y1]
            for x1 in range(len(line)):
                area = 0
                if ((x1, y1) not in self.visited):
                    if (self.nodes[y1][x1] == 1):
                        area = self.flood_fill(x1, y1)
                if (area > max_area):
                    max_area = area
        return max_area

    # Reference: https://en.wikipedia.org/wiki/Flood_fill
    def flood_fill(self, x, y):
        start = (x, y)
        queue = deque()
        total_area = 0
        self.visited.add((x, y))
        queue.append(start)
        while (len(queue) != 0):
            total_area += 1
            current = queue.popleft()
            self.fill_neighbors(queue, current)
        return total_area

    def fill_neighbors(self, queue, current):
        x1, y1 = current
        neighbors = [
            # top, right, bottom, left
            (1, 0), (0, 1), (0, -1), (-1, 0),
            # top-right, bottom-right, bottom-left, top-left
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        for a, b in neighbors:
            x2, y2 = x1 + a, y1 + b
            if (x2 >= 0 and x2 < self.width and y2 >= 0 and y2 < self.height):
                if (self.nodes[y2][x2] == 1 and (x2, y2) not in self.visited):
                    self.visited.add((x2, y2))
                    queue.append((x2, y2))


grid = Grid()
grid.read_input()
print(grid.get_biggest_region())
