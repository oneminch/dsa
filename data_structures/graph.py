class Graph:
    def __init__(self):
        self.num_vertices = 0
        self.adjacency_list = {}

    def __str__(self):
        return str(self.__dict__)

    def add_vertex(self, node):
        self.adjacency_list[node] = []
        self.num_vertices += 1
        
    def add_edge(self, node1, node2):
        if node1 not in self.adjacency_list or node2 not in self.adjacency_list:
            print("One of the nodes doesn't exist")

        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node1].sort()
        self.adjacency_list[node2].append(node1)
        self.adjacency_list[node2].sort()

    def show_adjacency_list(self):
        print("\nAdjacency List:\n")
        for node in self.adjacency_list:
            node_edges = self.adjacency_list[node]
            edges = ""
            for vertex in node_edges:
                edges += vertex + " "
            print(f"{node} --> {edges}")