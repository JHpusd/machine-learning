import sys
sys.path.append('src')
from matrix import Matrix

A = Matrix([[1, 3], [2, 4]])
B = A.copy()
A = "reset to string"
print("Testing method 'copy'...")
assert B.elements == [[1, 3], [2, 4]]
print("PASSED")

C = Matrix([[1, 0], [2, -1]])
D = B.add(C)
print("Test method 'add'...")
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
