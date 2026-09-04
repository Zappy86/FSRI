from manim import *
import networkx as nx


class CompleteBipartiteGraph(Scene):
    def construct(self):
        # Create K_{2,3}
        G = nx.complete_bipartite_graph(2, 3)

        # Position the vertices
        positions = {
            0: [-2, 1, 0],     # top left
            1: [-2, -1, 0],    # bottom left
            2: [2, 2, 0],      # top right
            3: [2, 0, 0],      # middle right
            4: [2, -2, 0],     # bottom right
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

        # Grey circle
        pebble = Circle(
            radius=0.22,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=.5,
            stroke_width=2,
        )

        # Start at the top-right vertex
        pebble.move_to(positions[2])
        self.add(pebble)

        # Top right -> top left
        self.play(
            pebble.animate.move_to(positions[0]),
            run_time=1,
        )

        # Top left -> bottom right
        self.play(
            pebble.animate.move_to(positions[4]),
            run_time=1,
        )

        self.wait(1)