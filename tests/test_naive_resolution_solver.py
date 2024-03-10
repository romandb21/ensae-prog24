import sys
sys.path.append("swap_puzzle/")
import unittest
from solver import Solver


class Test_NaiveResolution(unittest.TestCase):
    def test_grid1(self):
        g = Solver(4, 2,[[1, 2], [3, 4], [5, 7], [6, 8]])
        self.assertEqual(g.get_solution(),[((2, 1), (3, 0))])
        self.assertEqual(g.get_solution_f(), [((2, 1), (3, 1)), ((3, 1), (3,
        0)), ((2, 1), (3, 1))])
        T = ((2,1),(3,0))
        self.assertEqual(g.transfo(T),[((2, 1), (3, 1)), ((3, 1), (3, 0)),
        ((2, 1), (3, 1))])
        Z = ((0,0),(0,1))
        self.assertEqual(g.transfo(Z),[((0, 0), (0, 1))])
        self.assertEqual(g.transfo_seq([T, Z]), [((2, 1), (3, 1)), ((3, 1),
        (3, 0)), ((2, 1), (3, 1)), ((0, 0), (0, 1))] )


if __name__ == '__main__':
    unittest.main()