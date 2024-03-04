import matplotlib.pyplot as plt
from grid import Grid
from solver import Solver
from graph import Graph


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
    g.add_edge(0, i+1)

print(g)

print(g.bfs(1, 9))
"""
D = "/home/onyxia/ensae-prog24/input/"
F = D + "graph1.in"

gg = Graph.graph_from_file(F)
print(gg)


D = "/home/onyxia/ensae-prog24/input/"
F = D + "graph2.in"

ggg = Graph.graph_from_file(F)
print(ggg)
print(ggg.(4, 9))
