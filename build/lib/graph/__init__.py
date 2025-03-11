from graph.vertex import Vertex
import sys
sys.setrecursionlimit(1000000)


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex1, vertex2, weight): 
        if vertex1 not in self.graph:
            v1 = Vertex(vertex1)
            self.graph[vertex1] = v1 
        if vertex2 not in self.graph:
            v2 = Vertex(vertex2)
            self.graph[vertex2] = v2
        
        self.graph[vertex1].add_neighbor(vertex2, weight)

    def display(self):
        for vertex in self.graph:
            edges_str = ', '.join([f"{neighbor} (вес {weight})" for neighbor, weight in self.graph[vertex].neighbors.items()])
            print(f"{vertex} -> {edges_str}")
    
    def get_accessible_vertices(self, vertex, way=[]):
        return [neighbor for neighbor in self.graph[vertex].get_neighbors() if neighbor not in way]

    def get_vertices(self):
        return list(self.graph.keys())

    def get_weight(self, vertex1, vertex2):
        return self.graph[vertex1].get_neighbor_weight(vertex2)

    def calculate_way_weight(self, way):
        weight = 0
        for i in range(len(way) - 1):
            edge_weight = self.get_weight(way[i], way[i + 1])
            if edge_weight is not None:
                weight += edge_weight
        return weight

    
    