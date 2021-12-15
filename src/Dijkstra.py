from GraphInterface import GraphInterface


class Dijkstra:
    def __init__(self, src: int, dest: int, g: GraphInterface):
        self.src = src
        self.dest = dest
        self.graph: GraphInterface = g


    def run(self):

