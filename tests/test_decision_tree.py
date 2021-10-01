import sys
sys.path.append('src')
from decision_tree import *
'''
init_points = {'x': [(1,1), (1,2), (2,2), (2,3)], 'o': [(1,3), (1,4), (2,4)]}
dt = DecisionTree(init_points)
print("first test case")
print("initial points:", dt.point_dict)
print("initial entropy:", dt.entropy)
print("best split:", dt.get_best_split())

dt.fit()
print("fitted the tree")
print("prediction for (2,1):", dt.predict((2,1)))
print("prediction for (1,6):", dt.predict((1,5)))

init_points = {'o':[(2,1),(2,2),(3,1),(3,2)], 'x':[(3,3),(4,1),(4,2),(4,3),(5,1)]}
dt = DecisionTree(init_points)
print('\nsecond test case')
print("initial points:",dt.entropy)
print("best split:",dt.get_best_split())

dt.fit()
print("fitted the tree")
print("prediction for (1,1):", dt.predict((1,1)))
print("prediction for (2,3):", dt.predict((2,3)))
print("prediction for (4,4):", dt.predict((4,4)))
print("prediction for (5,2):", dt.predict((5,2)))

init_points = {'x':[(1,7),(2,7),(3,7),(3,8),(3,9),(7,1)], 'o':[(1,9),(5,1),(5,2),(5,3),(6,3),(7,3)]}
dt = DecisionTree(init_points, 7)
dt.fit()

assert dt.predict((1,6)) == 'x'
assert dt.predict((2,8)) == 'x'
assert dt.predict((3,10)) == 'x'
assert dt.predict((5,5)) == 'o'
assert dt.predict((6,2)) == 'o'
assert dt.predict((7,2)) == 'o'
assert len(dt.branches[0].branches) == 0
assert len(dt.branches[1].branches) == 0

init_points = {'x':[(1,3),(1,5),(2,4),(2,5)], 'o':[(1,4),(2,3)]}
dt = DecisionTree(init_points, 5)
dt.fit()

assert dt.predict((1,6)) == 'x'
assert dt.predict((2,6)) == 'x'
assert dt.predict((1,2)) == 'x' # random seeded
assert dt.predict((2,2)) == 'x' # random seeded
for branch in dt.branches:
    assert len(branch.branches) == 0
'''
init_points = {'x':[(0,1),(0,1),(0,2),(1,1),(1,2),(1,2)], 'o':[(0,2),(1,1),(1,1),(1,2)]}
dt= DecisionTree(init_points, 1)

<<<<<<< HEAD
dt.fit()

assert dt.predict((0,1)) == 'x'
assert dt.predict((1,1)) == 'o'
assert dt.predict((1,2)) == 'x'
assert dt.predict((0,2)) == 'x' # random seeded
for branch in dt.branches:
    for subbranch in branch.branches:
        assert len(subbranch.branches) == 0
=======
dt.split(get_best_split())
>>>>>>> origin/master
