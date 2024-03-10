import sys
sys.path.append("swap_puzzle/")
import unittest
from graph import Graph


class Test_GraphLoading(unittest.TestCase):
    def test_graph1(self):
        g = Graph.graph_from_file("input/graph1.in")
        self.assertEqual(g.nb_nodes, 20)
        self.assertEqual(g.nb_edges, 100)


if __name__ == '__main__':
    unittest.main()
