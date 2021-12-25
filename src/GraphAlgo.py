import concurrent.futures
import json
import math
import multiprocessing
import random
from itertools import islice
from typing import List

from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph

from src.GUI import Drawer


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: GraphInterface = None):
        self.graph: GraphInterface = g
        self.fake_pos = False

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
                self.fake_pos = True
                (px, py, pz) = (random.uniform(0, 1), random.uniform(0, 1), 0)
            g.add_node(n["id"], (px, py, pz))

        for n in js["Edges"]:
            g.add_edge(n["src"], n["dest"], n["w"])

        self.graph = g

    def save_to_json(self, file_name: str) -> bool:
        out = {
            "Nodes": [],
            "Edges": []
        }
        for n in self.graph.get_all_v().values():
            js = {}
            js["id"] = n.id
            if not self.fake_pos:
                js["pos"] = F"{n.loc[0]},{n.loc[1]},{n.loc[2]}"
            out["Nodes"].append(js)

        for n in self.graph.get_all_v():
            for e in self.graph.all_out_edges_of_node(n):
                out["Edges"].append({
                    "src": n,
                    "dest": e,
                    "w": self.graph.all_out_edges_of_node(n)[e],
                })

        f = open(file_name, "w+")
        f.write(str(out))

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        dist, prev = self.dijkstra(id1)
        ret = []
        p = prev[id2]
        while p != -1:
            ret.append(p)
            p = prev[p]

        ret.reverse()
        if len(ret) > 0:
            ret.append(id2)

        return dist[id2], ret

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if len(node_lst) == 0 or node_lst is None:
            return None
        ret_w = 0
        remaining = node_lst.copy()
        ret = [remaining[0]]
        while len(remaining) > 0:
            city = ret[-1]
            if city in remaining:
                remaining.remove(city)

            try:
                min_road, p = self.get_min_undirected_road(city, remaining)
            except KeyError:
                return False

            ret_w += p
            for n in min_road:
                if n in remaining:
                    remaining.remove(n)
                ret.append(n)
        return ret, ret_w

    def centerPoint(self) -> (int, float):
        ret = None
        min_dist = float('inf')

        chunk_size = 1
        nodes = self.to_chuncks(self.graph.get_all_v(),500)

        with concurrent.futures.ThreadPoolExecutor() as executer:
            res = [executer.submit(self.center_helper,node) for node in nodes]

            for f in concurrent.futures.as_completed(res):
                r = f.result()
                if r[1] < min_dist:
                    min_dist = r[1]
                    ret = r[0]

        return ret,min_dist

    def plot_graph(self) -> None:
        d = Drawer.Drawer(self)
        d.main()

    def dijkstra(self, src) -> (dict, dict):
        dist = {}
        prev = {}
        visited = []
        Q = []

        nodes = self.graph.get_all_v()
        for node_id in nodes:
            if node_id == src:
                dist[node_id] = 0
                prev[node_id] = -1
            else:
                dist[node_id] = float('inf')
                prev[node_id] = -1

        Q.append(src)

        while len(Q) != 0:
            sorted(Q, key=lambda x: dist[x])
            n = Q.pop()
            edges = self.graph.all_out_edges_of_node(n)
            for dest in edges:
                if dest in visited:
                    continue;
                alt = dist[n] + edges[dest]
                if alt < dist[dest]:
                    dist[dest] = alt
                    prev[dest] = n
                    Q.append(dest)

        return dist, prev

    def get_min_undirected_road(self, node, remaining):
        dist, prev = self.dijkstra(node)
        min_node = None
        min_weight = float('inf')
        for n in remaining:
            w = dist[n]
            if w < min_weight:
                min_weight = w;
                min_node = n

        ret = []
        p = prev[min_node]
        while p != -1 and p != node:
            ret.append(p)
            p = prev[p]
        ret.reverse()
        ret.append(min_node)
        return ret, dist[min_node]

    def center_helper(self,nodes):
        ret = None
        min_dist = float('inf')
        for n in nodes:
            dist, prev = self.dijkstra(n)
            m = max(dist, key=dist.get)
            if dist[m] < min_dist:
                min_dist = dist[m]
                ret = m
        return ret, min_dist

    '''
    This soultion was given here:
    https://stackoverflow.com/questions/22878743/how-to-split-dictionary-into-multiple-dictionaries-fast
    
    It takes a dictionary, and slices it to chunks.
    '''
    def to_chuncks(self,data, chunk_size):
        it = iter(data)
        for i in range(0, len(data), math.ceil(len(data)/chunk_size)):
            yield {k: data[k] for k in islice(it, math.ceil(len(data)/chunk_size))}
