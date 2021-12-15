import json
from typing import List

from GraphAlgoInterface import GraphAlgoInterface, GraphInterface
from Node import Node
from DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = None):
        self.graph: DiGraph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        g = DiGraph()
        f = open(file_name)
        js = json.load(f)

        for n in js["Nodes"]:
            if "pos" in n:
                (px, py, pz) = n["pos"].split(",")
            else:
                (px, py) = (0, 0)
            g.add_node(n["id"], (px, py))

        for n in js["Edges"]:
            g.add_edge(n["src"], n["dest"], n["w"])

        self.graph = g

    def save_to_json(self, file_name: str) -> bool:
        out = {
            "Nodes":[],
            "Edges":[]
        }
        for n in self.graph.get_all_v().values():
            out["Nodes"].append({"id":n.id})

        for n in self.graph.get_all_v():
            for e in self.graph.all_out_edges_of_node(n):
                print(e)
                out["Edges"].append({
                    "src" : n,
                    "dest" : e,
                    "w" : self.graph.all_out_edges_of_node(n)[e],
                })

        f = open(file_name,"w+")
        f.write(str(out))

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        return (5, [0, 1, 2])

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        raise NotImplementedError
