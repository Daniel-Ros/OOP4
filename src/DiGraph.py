import random

from src.GraphInterface import GraphInterface
from src.Node import Node

class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.mc = 0
        self.edges = 0

    def __repr__(self):
        return F"Graph: |V|={self.v_size()} , |E|={self.e_size()}"

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].edges_from

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].edges_to

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.edges

    def get_mc(self) -> int:
        self.mc += 1

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id2 not in self.nodes[id1].edges_to:
            self.edges += 1
            self.nodes[id1].edges_to[id2] = weight
            self.nodes[id2].edges_from[id1] = weight
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False

        if pos is None:
            pos = (random.uniform(0,1), random.uniform(0,1), 0)
        self.nodes[node_id] = Node(node_id, pos)
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes[node_id]:
            self.nodes[node_id] = None
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id2 in self.nodes[node_id1].edges_to:
            self.edges -= 1
            self.nodes[node_id1].edges_to.pop(node_id2)
            self.nodes[node_id2].edges_from.pop(node_id1)
            return True
        return False
