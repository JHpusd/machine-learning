import sys
sys.path.append('src')
from test_methods import *
from forest import *
sys.path.append('datasets')
from random_clusters import *

x_clusters = [(1,1), (4,4)]
o_clusters = [(1,4), (4,1)]

points = generate_clusters(x_clusters, o_clusters, 2, 4, 100)
points_copy = points.copy()

folds = mult_folds(5, points_copy)
'''
forest = Forest(10, folds[0], 1)
forest.init_trees()
forest.fit_trees()
print(forest.predict((1,4)))
'''
num_trees = [1,10,20,50,100,500,1000]
accuracies = []
for num in num_trees:
    acc = 0
    for fold in folds:
        training = get_training(folds, fold)
        forest = Forest(num, training, 1)
        forest.init_trees()
        forest.fit_trees()
        acc += correct_percent(forest, fold)
    accuracies.append(acc / len(folds))
print(accuracies)
plt.style.use('bmh')
plt.plot(num_trees, accuracies)
plt.xlabel('num trees')
plt.ylabel('5-fold accuracy')
plt.savefig('random_split_forest.png')

