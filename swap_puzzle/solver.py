from grid import Grid
from graph import Graph
from itertools import permutations

class Solver(Grid): 
    """
    A solver class, to be implemented.
    """
    def __init__(self, m, n, initial_state = []):
        super().__init__(m, n, initial_state = initial_state)

    



    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        (m , n) = (len(self.state), len(self.state[0]))
        
        L = []
        for i in range(m):
            L = L + self.state[i]
        A = len(L)
        L_swap = []
        print(L)

        for i in range(A):
            
            if (i+1)%n == 0:
                c_0 = (((i+1)//n)-1, n-1)

            else: 
                c_0 = (((i+1)//n), ((i+1)%n)-1)

            if L[i] != i+1:
                for j in range(i+1, A):
                    if L[j] == i+1:
                        if (j+1)%n == 0:
                            c_1 = (((j+1)//n)-1, n-1)
                        else : 
                            c_1 = (((j+1)//n), ((j+1)%n)-1)
                        L[i], L[j] = L[j], L[i]
                C = (c_0, c_1)
                L_swap.append(C)
        return L_swap
    #La complexité temporelle est en O(nm*(nm!))

    def transfo(self, T):
        """Transform an impossible swap in a sequence of possible swaps

         Args:
         T (_type_): tuple of two points (point = (i, j))
        """
        (i,j) = T[0]
        L = []
        while i != T[1][0]:
            if i > T[1][0]:
                L.append(((i,j), (i-1, j)))
                i = i - 1
            else:
                L.append(((i,j), (i+1, j)))
                i = i + 1
        while j != T[1][1]: 
            if j > T[1][1]:
                L.append(((i, j), (i, j-1)))
                j = j - 1
            else:
                L.append(((i, j), (i, j+1))) 
                j = j + 1
        L_f = L[:]   
       
        for k in range(1, len(L)):
            L_f.append(L[len(L)-1-k])
         
        return L_f

    def transfo_seq(self, L):
        """Transform a list of impossible swaps in a list of possible swaps

        Args:
                L (list): list of tuple [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 

        Returns:
                L_s (list): list of tuple [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        L_s = []
        for i in L:
            L_s = L_s + self.transfo(i)
        return L_s

    def get_solution_f(self):
        L = self.get_solution()
        L_f = self.transfo_seq(L)
        return L_f

    
        

