from collections import deque

class Graph:
    def __init__(self, nb_nodes, nb_edges, edge_length, edges):
        self.nb_nodes = nb_nodes
        self.nb_edges = nb_edges
        self.edge_length = edge_length
        self.edges = edges
        self.nodes = {}
        self.init_nodes()

    def init_nodes(self):
        for i in range(1, self.nb_nodes + 1):
            self.nodes[i] = set() # city identifier => edges
        for edge in self.edges:
            self.nodes[edge[0]].add(edge[1])
            self.nodes[edge[1]].add(edge[0])

    # Reference: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    def search(self, start_node):
        queue = deque()
        distances = {}
        queue.append(start_node)
        distances[start_node] = 0

        while (len(queue) != 0):
            id_next_node = queue.popleft()
            for id_neighbor in self.nodes[id_next_node]:
                if (id_neighbor not in distances):
                    distances[id_neighbor] = distances[id_next_node] + self.edge_length
                    queue.append(id_neighbor)

        return distances

    def print_distances(self, start_node):
        distances = self.search(start_node)
        for node in range(1, self.nb_nodes + 1):
            if (node != start_node):
                if (node in distances):
                    print(distances[node], end='')
                else:
                    print(-1, end='')
                if node != self.nb_nodes:
                    print(' ', end='')
        print()

nb_queries = int(input())
for i in range(nb_queries):
    nb_nodes, nb_edges = [int(value) for value in input().split()]
    edges = []
    for i in range(nb_edges):
        edge = [int(x) for x in input().split()]
        edges.append(edge)
    start_node = int(input())
    graph = Graph(nb_nodes, nb_edges, 6, edges)
    graph.init_nodes()
    graph.print_distances(start_node)
