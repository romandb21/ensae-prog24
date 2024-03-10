import sys
sys.path.append("swap_puzzle/")

import unittest
from grid import Grid


class Test_bfs_2(unittest.TestCase):
    def test_grid0(self):
        g = Grid.grid_from_file("input/grid0.in")
        self.assertEqual(g.bfs_2(), [((0, 1), (1, 1)), ((0, 0), (0, 1))])
    def test_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
    self.assertEqual(g.bfs_2(), [((3, 0), (3, 1))])

if __name__ == '__main__':
    unittest.main()