from manim import *
import networkx as nx


class CompleteBipartiteGraph(Scene):
    def construct(self):
        # Create K_{2,3}
        G = nx.complete_bipartite_graph(2, 3)

        # Position the vertices
        positions = {
            0: [-2, 1, 0],
            1: [-2, -1, 0],
            2: [2, 2, 0],
            3: [2, 0, 0],
            4: [2, -2, 0],
        }

        # Create the graph
        graph = Graph.from_networkx(
            G,
            layout=positions,
            labels=False,
            vertex_type=Circle,
            vertex_config={
                "radius": 0.3,
                "color": PURPLE,
                "fill_color": PURPLE,
                "fill_opacity": 1.0,
            },
            edge_config={
                "stroke_width": 6,
                "color": WHITE,
            },
        )

        self.add(graph)
        self.wait(1)