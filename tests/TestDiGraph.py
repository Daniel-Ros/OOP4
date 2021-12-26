from unittest import TestCase
from src.DiGraph import DiGraph

class TestDiGraph(TestCase):

    def test_get_all_v(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)

        self.assertEqual(len(g.get_all_v()),3)
        self.assertEqual(g.get_all_v()[0].id,0)
        self.assertEqual(g.get_all_v()[1].id,1)
        self.assertEqual(g.get_all_v()[2].id,2)

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)

        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)

        self.assertEqual(len(g.all_in_edges_of_node(0)), 1)
        self.assertEqual(g.all_in_edges_of_node(0)[1], 1.1)


    def test_all_out_edges_of_node(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)

        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)

        self.assertEqual(len(g.all_out_edges_of_node(0)), 1)
        self.assertEqual(g.all_out_edges_of_node(0)[1], 1)

    def test_v_size(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)

        self.assertEqual(g.v_size(), 4)

    def test_e_size(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)

        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)

        self.assertEqual(g.e_size(), 5)

    def test_get_mc(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)

        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)

        self.assertEqual(g.get_mc(), 9)

    def test_add_edge(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)

        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)

        self.assertEqual(len(g.all_in_edges_of_node(0)), 1)
        self.assertEqual(g.all_in_edges_of_node(0)[1], 1.1)

    def test_add_node(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)

        self.assertEqual(len(g.get_all_v()), 3)
        self.assertEqual(g.get_all_v()[0].id, 0)
        self.assertEqual(g.get_all_v()[1].id, 1)
        self.assertEqual(g.get_all_v()[2].id, 2)


    def test_remove_node(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)

        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)

        g.remove_node(0)
        g.remove_node(5)

        self.assertEqual(len(g.get_all_v()), 2)
        self.assertEqual(g.e_size(), 1)


    def test_remove_edge(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)

        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)

        g.remove_edge(0,1)

        self.assertEqual(g.e_size(), 2)
        self.assertEqual(g.remove_edge(0,1), False)

