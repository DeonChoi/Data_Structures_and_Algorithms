#implementation of an undirected graph using Adjacency Lists
class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = []
    
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))

g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()

#implementation of an undirected graph using Adjacency Matrix, with weighted or unweighted edges
class Vertex1:
    def __init__(self, n):
        self.name = n

class Graph1:
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex1) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight = 1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False
    
    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end = '')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end = '')
            print(' ')

g1 = Graph1()
a1 = Vertex1('A')
g1.add_vertex(a1)
g1.add_vertex(Vertex1('B'))
for i in range(ord('A'), ord('K')):
    g1.add_vertex(Vertex1(chr(i)))

edges1 = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges1:
    g1.add_edge(edge[:1], edge[1:])

g1.print_graph()

