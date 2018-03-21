#!/bin/python3

import sys

class Graph:
    def __init__(self, nb_cities, nb_roads, cost_library, cost_road, roads):
        self.nb_cities = nb_cities
        self.nb_roads = nb_roads
        self.cost_library = cost_library
        self.cost_road = cost_road
        self.roads = roads
        self.cities = {}
        self.init_nodes()

    def init_nodes(self):
        for i in range(1, self.nb_cities + 1):
            self.cities[i] = set() # city identifier => roads
        for road in self.roads:
            self.cities[road[0]].add(road[1])
            self.cities[road[1]].add(road[0])

    def dfs(self, id_city):
        visited = set()
        stack = []
        visited.add(id_city)
        stack.append(id_city)

        while (len(stack) != 0):
            id_next_city = stack.pop()
            for id_neighbor in self.cities[id_next_city]:
                if (id_neighbor not in visited):
                    visited.add(id_neighbor)
                    stack.append(id_neighbor)

        return visited

    def extract_connected_components(self):
        connected_components = []
        all_cities_visited = set()

        for id_city in range(1, self.nb_cities + 1):
            if (id_city not in all_cities_visited):
                visited = self.dfs(id_city)
                all_cities_visited.update(visited)
                connected_components.append(visited)

        return connected_components

    def roads_and_libraries(self):
        if (self.cost_road >= self.cost_library):
            return nb_cities * self.cost_library
        else:
            total_cost = 0
            for connected_component in self.extract_connected_components():
                total_cost += (len(connected_component) - 1) * self.cost_road + self.cost_library
            return total_cost

if __name__ == "__main__":
    nb_queries = int(input().strip())
    for _ in range(nb_queries):
        nb_cities, nb_roads, cost_library, cost_road = map(int, input().strip().split())
        roads = []
        for _ in range(nb_roads):
           road = list(map(int, input().strip().split()))
           roads.append(road)
        graph = Graph(nb_cities, nb_roads, cost_library, cost_road, roads)
        print(graph.roads_and_libraries())
