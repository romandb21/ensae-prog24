import unittest
from grid import Grid


class Test_A_etoile_naif(unittest.TestCase):
    def test_grid0(self):
        s = Grid.grid_from_file("input/grid0.in")
        g = Grid(2,2,[[2,1], [3,4]])
        f = Grid(2,2)
        t1 = s.grid_to_tuple()
        t2 = g.grid_to_tuple()
        t3 = f.grid_to_tuple()
        self.assertEqual(f.A_etoile_naif(s),[t1,t2,t3])

if __name__ == '__main__':
    unittest.main()