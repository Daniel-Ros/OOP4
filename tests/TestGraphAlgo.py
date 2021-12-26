from math import inf
from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        ga = GraphAlgo()
        self.assertEqual(ga.get_graph(),None)
        ga.load_from_json("../data/A0.json")
        self.assertNotEqual(ga.get_graph(),None)

    def test_load_from_json(self):
        ga = GraphAlgo()
        self.assertEqual(ga.get_graph(), None)
        self.assertEqual(ga.load_from_json("../data/A0.json"), True)
        self.assertNotEqual(ga.get_graph(), None)
        self.assertEqual(ga.load_from_json("../data/jasedbhflkjhsdgbfljkhasgbdflkhgasdlfkhgasdf.json"), False)

    def test_save_to_json(self):
        ga = GraphAlgo()
        self.assertEqual(ga.get_graph(), None)
        ga.load_from_json("../data/A0.json")
        self.assertNotEqual(ga.get_graph(), None)
        self.assertEqual(ga.save_to_json("../data/SaveTest.json"), True)

    def test_shortest_path(self):
        ga = GraphAlgo()
        file = "../data/T0.json"
        ga.load_from_json(file)  # init a GraphAlgo from a json file
        self.assertEqual(ga.shortest_path(3, 1), (3.4, [0, 1, 2, 3]))
        self.assertEqual(ga.shortest_path(0, 3), (inf, []))



    def test_tsp(self):
        ga = GraphAlgo()
        ga.load_from_json('../data/A5.json')
        self.assertEqual(ga.TSP([1, 2, 3]),([1, 9, 2, 3], 2.370613295323088))

    def test_center_point(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/A5.json")
        print(ga.centerPoint())


    def test_dijkstra(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(4)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1)
        ga = GraphAlgo(g)
        dist,prev = ga.dijkstra(0)
        self.assertEqual(dist[1],1)
        self.assertEqual(dist[4],float('inf'))
        self.assertEqual(prev[1], 0)
        self.assertEqual(prev[4], -1)

    def test_get_min_undirected_road(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(4)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1)
        g.add_edge(1, 4, 1)
        ga = GraphAlgo(g)
        self.assertEqual(ga.get_min_undirected_road(0,[1,4]),([1],1))
        self.assertEqual(ga.get_min_undirected_road(0,[4]),([1,4],2))

    def test_is_connected(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        ga = GraphAlgo(g)
        self.assertEqual(ga.is_connected(),False)
        g.add_edge(0,1,1)
        self.assertEqual(ga.is_connected(),False)
        g.add_edge(1,0,1)
        self.assertEqual(ga.is_connected(), True)

