from .graph import Graph


class Tree(Graph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, directed=True)

    def get_children(self, node_name: str):
        # returns the children of a node
        node_id = self.gen[node_name]
        neighbors = self.graph.neighbors(node_id, mode="out")

        # Change from indices to names
        neighbors = [self.gen.reverse_dict()[index] for index in neighbors]

        return neighbors
