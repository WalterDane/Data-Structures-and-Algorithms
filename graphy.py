"""
Formal Definition: A graph is a pair of sets (V, E) where V is the set of
vertices and E is the set of edges, connecting the pairs of vertices
"""

class Vertex():
    def __init__(self, data):
        self.data = data

class Edge():
    def __init__(self, weight = None):
        self.weight = weight

class Graph():
    def __init__(self):
        pass

    def add_vertex(self, node):
        """
        adds a vertex to the graph
        """
        pass

    def add_edge(self, node1, node2):
        """
        adds an edge between the two vertices of the graph
        """
        pass

    def remove_vertex(self, node):
        """
        removes a specified vertex
        """
        pass

    def remove_edge(self, edge):
        pass

    def contains(self, node):
        """
        checks to see if the graph contains a certain vertex
        """
        pass

    def has_edge(self, node1, node2):
        """
        checks to see if their is a connection between any two vertices
        """
        pass