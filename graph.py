"""
Formal Definition: A graph is a pair of sets (V, E) where V is the set of
vertices and E is the set of edges, connecting the pairs of vertices
"""

class Vertex():
    def __init__(self, data = None, label = None):
        self.label = label
        self.data = data

class Edge():
    def __init__(self, weight = None):
        self.weight = weight

class Graph():
    def __init__(self):
        self.label = 0
        self.adjacency_matrix = []

    def add_vertex(self, vertex):
        """
        adds a vertex to the graph
        """
        if self.label == 0:
            vertex.label = 0
            self.adjacency_matrix.append([0])
            self.label += 1
        else:
            vertex.label = self.label
            for each in self.adjacency_matrix:
                each.append(0)
            self.adjacency_matrix.append([0] * len(self.adjacency_matrix[0]))
            self.label += 1

    def add_edge(self, vertex1, vertex2):
        """
        adds an edge between the two vertices of the graph
        """
        self.adjacency_matrix[vertex1.label][vertex2.label] = 1
        self.adjacency_matrix[vertex2.label][vertex1.label] = 1
        print(self.adjacency_matrix)
        
    def remove_vertex(self, vertex):
        """
        removes a specified vertex
        """
        pass

    def remove_edge(self, edge):
        pass

    def contains(self, vertex):
        """
        checks to see if the graph contains a certain vertex
        """
        pass

    def has_edge(self, vertex1, vertex2):
        """
        checks to see if their is a connection between any two vertices
        """
        pass

vertex1 = Vertex("Elon Musk")
vertex2 = Vertex("Jeff Bezos")
vertex3 = Vertex("Mark Zuckerberg")
graph = Graph()
graph.add_vertex(vertex1)
graph.add_vertex(vertex2)
graph.add_vertex(vertex3)
graph.add_edge(vertex2, vertex3)