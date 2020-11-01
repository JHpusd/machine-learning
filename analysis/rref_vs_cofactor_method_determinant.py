import sys
sys.path.append('src')
from matrix import Matrix

ten_by_ten = []
counter = 1
for i in range(10):
    ten_by_ten.append([])
    for j in range(10):
        ten_by_ten[i].append(counter)
        counter += 1
tbt = Matrix(ten_by_ten)

rref_ans = tbt.determinant()
print(rref_ans)

cbt_ans = tbt.cofactor_method_determinant()
print(cbt_ans)

# the rref method is a lot faster, because it doesn't require recursion over and over and over again. (especially important when we have something as big as a 10x10 matrix)
