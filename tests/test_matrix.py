import sys
sys.path.append('src')
from matrix import Matrix
'''
# Matrix operations
A = Matrix([[1, 3], [2, 4]])
B = A.copy()
A = "reset to string"
print("Testing method 'copy'...")
assert B.elements == [[1, 3], [2, 4]]
print("PASSED")

C = Matrix([[1, 0], [2, -1]])
D = B.add(C)
print("Testing method 'add'...")
assert D.elements == [[2, 3], [4, 3]]
print("PASSED")

E = B.subtract(C)
print("Testing method 'subtract'...")
assert E.elements == [[0, 3], [0, 5]]
print("PASSED")

F = B.scalar_multiply(2)
print("Testing method 'scalar_multiply'...")
assert F.elements == [[2, 6], [4, 8]]
print("PASSED")

G = B.matrix_multiply(C)
print("Testing method 'matrix_multiply'...")
assert G.elements == [[7, -3], [10, -4]]
print("PASSED")

# Generalized functions & transposed functions
A = Matrix([[1, 0, 2, 0, 3], [0, 4, 0, 5, 0], [
    6, 0, 7, 0, 8], [-1, -2, -3, -4, -5]])
print("Testing attributes 'num_rows' and 'num_cols'...")
assert (A.num_rows, A.num_cols) == (4, 5)
print("PASSED")
A_t = A.transpose()
print("Testing method 'transpose'...")
assert A_t.elements == [[1, 0, 6, -1], [0, 4, 0, -2], [
    2, 0, 7, -3], [0, 5, 0, -4], [3, 0, 8, -5]]
print("PASSED")
print("Testing that methods work on transposed function...")
B = A_t.matrix_multiply(A)
assert B.elements == [[38, 2, 47, 4, 56], [2, 20, 6, 28, 10], [
    47, 6, 62, 12, 77], [4, 28, 12, 41, 20], [56, 10, 77, 20, 98]]
C = B.scalar_multiply(0.1).round(5)
assert C.elements == [[3.8, .2, 4.7, .4, 5.6], [
    .2, 2.0, .6, 2.8, 1.0], [4.7,  .6, 6.2, 1.2, 7.7], [
        .4, 2.8, 1.2, 4.1, 2.0], [5.6, 1.0, 7.7, 2.0, 9.8]]
D = B.subtract(C)
assert D.elements == [[34.2, 1.8, 42.3, 3.6, 50.4], [
    1.8, 18., 5.4, 25.2, 9.], [42.3, 5.4, 55.8, 10.8, 69.3], [
        3.6, 25.2, 10.8, 36.9, 18.], [50.4, 9., 69.3, 18., 88.2]]
E = D.add(C)
assert E.elements == [[38, 2, 47, 4, 56], [2, 20, 6, 28, 10], [
    47, 6, 62, 12, 77], [4, 28, 12, 41, 20], [
        56, 10, 77, 20, 98]]
assert (E.is_equal(B), E.is_equal(C)) == (True, False)
print("ALL PASSED")

# Row reduction
print("Testing row reduction on [[0, 1, 2], [3, 6, 9], [2, 6, 8]]...")
A = Matrix([[0, 1, 2], [3, 6, 9], [2, 6, 8]])
print("Testing method 'get_pivot_row(0)'...")
assert A.get_pivot_row(0) == 1
print("PASSED")
print("Testing method 'swap_rows(0, 1)'...")
A = A.swap_rows(0, 1)
assert A.elements == [[3, 6, 9], [0, 1, 2], [2, 6, 8]]
print("PASSED")
print("Testing method 'normalize_row(0)'...")
A = A.normalize_row(0)
assert A.elements == [[1, 2, 3], [0, 1, 2], [2, 6, 8]]
print("PASSED")
print("Testing method 'clear_below(0)'...")
A = A.clear_below(0)
assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 2, 2]]
print("PASSED")
print("Testing method 'get_pivot_row(1)'...")
assert A.get_pivot_row(1) == 1
print("PASSED")
print("Testing method 'normalize_row(1)'...")
A = A.normalize_row(1)
assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 2, 2]]
print("PASSED")
print("Testing method 'clear_below(1)'...")
A = A.clear_below(1)
assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 0, -2]]
print("PASSED")
print("Testing method 'get_pivot_row(2)'...")
assert A.get_pivot_row(2) == 2
print("PASSED")
print("Testing method 'normalize_row(2)'...")
A = A.normalize_row(2)
assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 0, 1]]
print("PASSED")
print("Testing method 'clear_above(2)'...")
A = A.clear_above(2)
assert A.elements == [[1, 2, 0], [0, 1, 0], [0, 0, 1]]
print("PASSED")
print("Testing method 'clear_above(1)'...")
A = A.clear_above(1)
assert A.elements == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print("PASSED")

print("Testing method 'rref()'...")
A = Matrix([[0, 1, 2], [3, 6, 9], [2, 6, 8]])
A = A.rref()
assert A.elements == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
B = Matrix([[0, 0, -4, 0], [0, 0, 0.3, 0], [0, 2, 1, 0]])
B = B.rref()
assert B.elements == [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
print("PASSED")

A = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
B = Matrix([[13, 14], [15, 16], [17, 18]])
A_augmented = A.augment(B)
print("Testing method 'augment'...")
assert A_augmented.elements == [
    [1, 2, 3, 4, 13, 14], [5, 6, 7, 8, 15, 16], [9, 10, 11, 12, 17, 18]]
print("PASSED")
print("Testing method 'get_rows'...")
rows_02 = A_augmented.get_rows([0, 2])
assert rows_02.elements == [
    [1, 2, 3, 4, 13, 14], [9, 10, 11, 12, 17, 18]]
print("PASSED")
print("Testing method 'get_columns'...")
cols_0123 = A_augmented.get_columns([0, 1, 2, 3])
assert cols_0123.elements == [
    [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print("PASSED")

# Inverse operations
print("Testing method 'inverse'...")
A = Matrix([[1, 2], [3, 4]])
A_inv = A.inverse()
assert A_inv.elements == [[-2, 1], [1.5, -0.5]]
A = Matrix([[1, 2, 3], [1, 0, -1], [0.5, 0, 0]])
A_inv = A.inverse()
assert A_inv.elements == [[0, 0, 2], [0.5, 1.5, -4], [0, -1, 2]]
A = Matrix([[1, 2, 3, 0], [1, 0, 1, 0], [0, 1, 0, 0]])
print("Expecting error...")
A_inv = A.inverse()
print("Expecting error...")
A = Matrix([[1, 2, 3], [3, 2, 1], [1, 1, 1]])
A_inv = A.inverse()
print("PASSED")
'''
# Determinants
print("Testing method 'determinant'...")
A = Matrix([[1, 2], [3, 4]])
ans = A.determinant()
assert round(ans, 6) == -2
A = Matrix([[1, 2 ,0.5], [3, 4, -1], [8, 7, -2]])
ans = A.determinant()
assert round(ans, 6) == -10.5
A = Matrix([[1,2,0.5,0,1,0], [3,4,-1,1,0,1], [8,7,-2,1,1,1], [
    -1,1,0,1,0,1], [0,0.35,0,-5,1,1], [1,1,1,1,1,0]])
ans = A.determinant()
assert round(ans, 6) == -37.3
A = Matrix([[1,2,0.5,0,1,0], [3,4,-1,1,0,1], [8,7,-2,1,1,1], [
    -1,1,0,1,0,1], [0,0.35,0,-5,1,1], [1,1,1,1,1,0], [2,3,1.5,1,2,0]])
ans = A.determinant()
print("Expecting error...")
print(ans)
A = Matrix([[1,2,0.5,0,1,0,1], [3,4,-1,1,0,1,0], [8,7,-2,1,1,1,0], [
    -1,1,0,1,0,1,0], [0,0.35,0,-5,1,1,0], [1,1,1,1,1,0,0], [
        2,3,1.5,1,2,0,1]])
ans = A.determinant()
assert round(ans, 6) == 0
print("PASSED")
