import sys, time
sys.path.append('src')
from decision_tree import *
sys.path.append('datasets')
from random_clusters import *

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

init_points = {'x':[(0,1),(0,1),(0,2),(1,1),(1,2),(1,2)], 'o':[(0,2),(1,1),(1,1),(1,2)]}
dt= DecisionTree(init_points, 1)

dt.fit()

assert dt.predict((0,1)) == 'x'
assert dt.predict((1,1)) == 'o'
assert dt.predict((1,2)) == 'x'
assert dt.predict((0,2)) == 'x' # random seeded
for branch in dt.branches:
    for subbranch in branch.branches:
        assert len(subbranch.branches) == 0
'''
x_clusters = [(1,1), (4,4)]
o_clusters = [(1,4), (4,1)]

points = generate_clusters(x_clusters, o_clusters, 2, 4, 100)
points_copy = points.copy()

def dict_remove(input_dict, key, item):
    copy = input_dict.copy()
    new_items = copy[key].remove(item)
    copy[key] = new_items
    return copy

def get_all_vals(point_dict):
    result = []
    for key in point_dict:
        result += point_dict[key]
    return result

def random_fold(point_dict, size):
    keys = list(point_dict.keys())
    result = {key:[] for key in keys}
    for _ in range(size):
        r_key = keys[r.randint(0,len(keys)-1)]
        if len(point_dict[r_key]) == 0:
            keys.remove(r_key)
            r_key = keys[r.randint(0,len(keys)-1)]
        items = point_dict[r_key]
        r_item = items[random.randint(0,len(items)-1)]
        result[r_key].append(r_item)
        dict_remove(point_dict, r_key, r_item)
    return result

def mult_folds(num_times, point_dict):
    fold_dicts = []
    fold_size = len(get_all_vals(point_dict)) / num_times
    assert int(fold_size) == fold_size, "num_times is incompatible"
    for _ in range(num_times):
        fold_dicts.append(random_fold(point_dict, int(fold_size)))
    return fold_dicts

def add_point_dicts(point_dict_list):
    # too lazy to add any more asserts
    result = {key:[] for key in point_dict_list[0]}
    for point_dict in point_dict_list:
        for key in point_dict:
            result[key] += point_dict[key]
    return result

def correct_percent(fitted_tree, test_point_dict):
    total = 0
    correct = 0
    for key in test_point_dict:
        for coord in test_point_dict[key]:
            if fitted_tree.predict(coord) == key:
                correct += 1
            total += 1
    return correct / total

def get_training(all_folds, excluded_fold):
    point_dict_list = [fold for fold in all_folds if fold != excluded_fold]
    return add_point_dicts(point_dict_list)

folds = mult_folds(5, points_copy)

min_sizes = [1,2,5,10,15,20,30,50,100]
correct_percentages = []
for min_size in min_sizes:
    avg_correct = 0
    for fold in folds:
        train = get_training(folds, fold)
        dt = DecisionTree(train, min_size)
        dt.fit()
        avg_correct += correct_percent(dt, fold)
    avg_correct /= len(folds)
    correct_percentages.append(avg_correct)

plt.style.use('bmh')
plt.plot(min_sizes, correct_percentages)
#plt.xlim(1,100)
#plt.ylim(0,1)
plt.xlabel('min_size_to_split')
plt.ylabel('5-fold accuracy')
plt.savefig('min_size_vs_accuracy.png')
