import sys
from simplex_alg import *


M = [[3,2,5,55], [2,1,1,26], [1,1,3,30], [5,2,4,57], [20,10,15,0]]
simplex = SimplexAlg(M)

simplex.solve()
print(simplex.matrix)
print(simplex.objective_val())