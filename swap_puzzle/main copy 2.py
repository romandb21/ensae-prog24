
import matplotlib.pyplot as plt
from grid import Grid
from solver import Solver
from graph import Graph
import copy
from itertools import permutations
"""
g = Grid(2, 3)
print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)

a=Grid(2, 3)

print(a)
print(a.is_sorted())

L = [((0, 0), (0,1)), ((1, 0), (1,1))]

a.swap_seq(L)
print(a)

a = Solver(2, 3)
a.swap((0,0), (1, 2))
print(a)

g = Graph([i for i in range(10)])
for i in range(9):
    g.add_edge(i, i+1)

print(g)

print(g.bfs(0, 9))
L = list(permutations(range(1, 7), 6))
print(L)

import heapq 
L = [(2, 3), (4, 6), (1, 9)]
heapq.heapify(L)
a, b = heapq.heappop(L)
print(L)
print(a)
print(b)
"""




