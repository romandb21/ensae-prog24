
import matplotlib.pyplot as plt
from grid import Grid
from solver import Solver
from graph import Graph
import copy
from itertools import permutations

g_ord = Grid(2, 3)

data_path = "/home/onyxia/ensae-prog24-1/input/"
file_name = data_path + "grid0.in"
g0 = Grid.grid_from_file(file_name)

data_path = "/home/onyxia/ensae-prog24-1/input/"
file_name = data_path + "grid1.in"
g1 = Grid.grid_from_file(file_name)

data_path = "/home/onyxia/ensae-prog24-1/input/"
file_name = data_path + "grid2.in"
g2 = Grid.grid_from_file(file_name)

data_path = "/home/onyxia/ensae-prog24-1/input/"
file_name = data_path + "grid3.in"
g3 = Grid.grid_from_file(file_name)

data_path = "/home/onyxia/ensae-prog24-1/input/"
file_name = data_path + "grid4.in"
g4 = Grid.grid_from_file(file_name)



#for i in Grid(2, 2).A_etoile_naif(g0):
#    print(i)
L = Grid(4, 4).A_etoile_naif(g4)
for i in L :
    print(i)