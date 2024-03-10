import sys
sys.path.append("swap_puzzle/")

import unittest
from graph import Graph


class Test_bfs(unittest.TestCase):
    def test_graph2(self):
        g = Graph.graph_from_file("input/graph2.in")
        self.assertEqual(g.bfs(2,9), [2,17, 7,9])
        self.assertEqual(g.bfs(4,13), [4, 18, 17, 7, 13])
        self.assertEqual(g.bfs(4,14), None)

if __name__ == '__main__':
    unittest.main()