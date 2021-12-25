from unittest import TestCase

from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        self.fail()

    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        self.fail()

    def test_tsp(self):
        self.fail()

    def test_center_point(self):
        ga = GraphAlgo()
        ga.load_from_json("../data/Test1.json")
        print(ga.centerPoint())

    def test_plot_graph(self):
        self.fail()

    def test_dijkstra(self):
        self.fail()

    def test_get_min_undirected_road(self):
        self.fail()

    def test_center_helper(self):
        self.fail()

    def test_to_chuncks(self):
        self.fail()
