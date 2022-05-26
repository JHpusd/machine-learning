from simplex_alg import *

matrix_rep = [[3,2,5,55],[2,1,1,26],[1,1,3,30],[5,2,4,57],[20,10,15,0]]
sa = SimplexAlg(matrix_rep)

print(sa.solutions())

matrix_rep = [[2,1,1,14],[4,2,3,28],[2,5,5,30],[1,2,1,0]]
sa = SimplexAlg(matrix_rep)

print(sa.solutions())
