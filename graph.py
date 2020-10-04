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
        removes the vertex from the adjacency matrix
        """
        self.adjacency_matrix.pop(vertex.label)
        for row in self.adjacency_matrix:
            row.pop(vertex.label)
        print(self.adjacency_matrix)
        pass

    def remove_edge(self, vertex1, vertex2):
        """
        removes the edge from the adjaceny matrix
        """
        self.adjacency_matrix[vertex1.label][vertex2.label] = 0
        self.adjacency_matrix[vertex2.label][vertex1.label] = 0

    def contains(self, label):
        """
        checks to see if the graph contains a certain vertex
        """
        try:
            self.adjacency_matrix[label]
        except IndexError:
            print("The graph does not contain the vertex")
        else:
            print("The graph contains the vertex")

    def has_edge(self, vertex1, vertex2):
        """
        checks to see if there is a connection between the two specified vertices
        """
        try:
            self.adjacency_matrix[vertex1][vertex2]
        except IndexError:
            print("The graph does not contain the edge")
        else:
            print("The graph contains the edge")