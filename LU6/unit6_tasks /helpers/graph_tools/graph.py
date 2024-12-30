import igraph as ig
import copy


class Graph:
    def __init__(
            self, graph: dict, plot_graph=True, simplify_graph=True,
            directed=False
    ) -> None:
        """
        Wrapper class for igraph.Graph. It takes a dictionary  and creates
        a graph from it.

        Args:
            graph (dict): Dictionary of the form {node_name: [children_names]}
            simplify_graph (bool, optional): If True, the graph is simplified
              so that duplicate edges are removed. Defaults to True.
            plot_graph (bool, optional): If True, the graph will be visualized
              as graph.png. Defaults to True.
        """

        # using igraph for Graph
        self.gen = ig.UniqueIdGenerator()
        self.graph = ig.Graph(edges=[(self.gen[v], self.gen[a])
                              for v in graph.keys() for a in graph[v]],
                              directed=directed)

        # set the names as attributes
        self.graph.vs["state"] = self.gen.values()

        # simplify the graph
        if simplify_graph:
            self.graph.simplify()

        # plot the graph for debugging
        if plot_graph:
            # set the labels to be the letters of the alphabet
            alphabet_letters = list(map(chr, range(97, 123)))
            self.graph.es["label"] = alphabet_letters

            ig.plot(self.graph, "graph.png", vertex_label=self.gen.values())

    def get_neighbors(self, node_name: str):
        # returns the neighbors of a node
        node_id = self.gen[node_name]
        neighbors = self.graph.neighbors(node_id)

        # Change from indices to names
        neighbors = [self.gen.reverse_dict()[index] for index in neighbors]

        return neighbors


class GraphWithWeights(Graph):
    def __init__(self, graph: dict, plot_graph=True) -> None:
        # remove weight numbers from node names
        base_graph = copy.copy(graph)
        for key in base_graph.keys():
            # remove the number, representing the weight
            base_graph[key] = [name.split(",")[0] for name in base_graph[key]]

        # initialize the base class
        super().__init__(base_graph, plot_graph=False)

        # add weights to the edges
        for start in base_graph.keys():
            for index, destination in enumerate(base_graph[start]):
                start_id = self.gen[start]
                destination_id = self.gen[destination]
                e_id = self.graph.get_eid(
                    start_id, destination_id)  # get the edge id
                weight = graph[start][index].split(",")[1]  # get the weight
                self.graph.es[e_id]["weight"] = weight

        # plot the graph for debugging
        if plot_graph:
            # set the labels to the weights
            self.graph.es["label"] = self.graph.es["weight"]
            ig.plot(self.graph, "graph.png",
                    vertex_label=self.gen.values())

    def get_cost(self, start, end):
        start_id = self.gen[start]
        end_id = self.gen[end]
        return self.graph.es[start_id, end_id]["weight"]
