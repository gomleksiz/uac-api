class WorkflowsVertexPositions():
    def __init__(self, egdes) -> None:
        self.edges = egdes
        self.positions = {}
        self.next_leaf_x_position = 0

    def calculate_positions(self, node, level=0):
        children = list(self.G.successors(node))
        if not children:
            # Leaf node, assign X position and increment the counter
            self.positions[node] = (self.next_leaf_x_position, level)
            self.next_leaf_x_position += 1
            return self.positions[node]
        else:
            # Calculate positions for children and determine this node's position
            child_positions = [self.calculate_positions(child, level + 1) for child in children]
        
            x_positions = [pos[0] for pos in child_positions]
            # # Parent's X is the average of its children's X positions
            # x_position = sum(x_positions) / len(x_positions)
            # self.positions[node] = (x_position, level)
            # Centering Logic
            leftmost_child_x = min(x_positions)
            rightmost_child_x = max(x_positions)
            center_x = (leftmost_child_x + rightmost_child_x) / 2  
            self.positions[node] = (center_x, level)
            return self.positions[node]

    def get_vertex_positions(self):
        try:
            import networkx as nx
        except ImportError:
            raise ImportError('This feature requires the networkx package. ' 
                            'You can install it via pip: pip install networkx')
        
        self.G = nx.DiGraph()
        for edge in self.edges:
            self.G.add_edge(edge['sourceId']['value'], edge['targetId']['value'])

        root_nodes = [n for n, d in self.G.in_degree() if d == 0]
        for root in root_nodes:
            self.calculate_positions(root)

        return self.positions
    