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

    '''
    return a dictionary of all the nodes in the Graph, each node is represented using a pair
     (node_id, node_data)
    '''
    def get_all_v(self) -> dict:
        return self.nodes
    '''
    return a dictionary of all the nodes connected to (into) node_id ,
    each node is represented using a pair (other_node_id, weight)
    '''
    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].edges_from
    '''
    return a dictionary of all the nodes connected from (from) node_id ,
    each node is represented using a pair (other_node_id, weight)
    
    '''
    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].edges_to

    '''
    Returns the number of vertices in this graph
    @return: The number of vertices in this graph
    '''
    def v_size(self) -> int:
        return len(self.nodes)

    '''
    Returns the number of edges in this graph
    @return: The number of edges in this graph
    '''
    def e_size(self) -> int:
        return self.edges
    '''
    Returns the current version of this graph,
    on every change in the graph state - the MC should be increased
    @return: The current version of this graph.    
    '''
    def get_mc(self) -> int:
        return self.mc
    '''
    Adds an edge to the graph.  
    @param id1: The start node of the edge
    @param id2: The end node of the edge
    @param weight: The weight of the edge
    @return: True if the edge was added successfully, False o.w.
    Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
    '''
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id2 not in self.nodes[id1].edges_to:
            self.edges += 1
            self.nodes[id1].edges_to[id2] = weight
            self.nodes[id2].edges_from[id1] = weight
            self.mc += 1
            return True
        return False

    '''
    Adds a node to the graph.
    @param node_id: The node ID
    @param pos: The position of the node
    @return: True if the node was added successfully, False o.w.
    Note: if the node id already exists the node will not be added
    '''
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False

        if pos is None:
            pos = (random.uniform(0,1), random.uniform(0,1), 0)
        self.nodes[node_id] = Node(node_id, pos)
        self.mc += 1
        return True
    '''
    Removes a node from the graph.
    @param node_id: The node ID
    @return: True if the node was removed successfully, False o.w.
    Note: if the node id does not exists the function will do nothing
    '''
    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            rem = []
            for e in self.all_out_edges_of_node(node_id):
                rem.append((node_id, e))
            for e in self.all_in_edges_of_node(node_id):
                rem.append((e,node_id))

            for r in rem:
                self.remove_edge(r[0],r[1])

            self.nodes.pop(node_id)
            return True
        else:
            return False
    '''
    Removes an edge from the graph.
    @param node_id1: The start node of the edge
    @param node_id2: The end node of the edge
    @return: True if the edge was removed successfully, False o.w.
    Note: If such an edge does not exists the function will do nothing
    '''
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id2 in self.nodes[node_id1].edges_to:
            self.edges -= 1
            self.nodes[node_id1].edges_to.pop(node_id2)
            self.nodes[node_id2].edges_from.pop(node_id1)
            return True
        return False
