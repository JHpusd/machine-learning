import sys
from sklearn.ensemble import RandomForestClassifier
sys.path.append('src')
from test_methods import *
from forest import *
sys.path.append('datasets')
from random_clusters import *

x_clusters = [(1,1), (4,4)]
o_clusters = [(1,4), (4,1)]

points = generate_clusters(x_clusters, o_clusters, 2, 2, 100)
points_copy = points.copy()

# x label is 1, o is 2

#folds = mult_folds(5, points_copy)
#num_trees = [1,10,20,50,100,500,1000]
'''
forest = Forest(10, folds[0], 1)
forest.init_trees()
forest.fit_trees()
print(forest.predict((1,4)))

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

# with sklearn

correct_percent = []
for num in num_trees:
    folds_correct_avg = 0
    for fold in folds:
        train = point_dict_to_lists(get_training(folds, fold))
        test = point_dict_to_lists(fold)
        X = train[0]
        y = train[1]
        x_test = test[0]
        y_test = test[1]
        forest = RandomForestClassifier(n_estimators=num)
        forest.fit(X,y)
        predictions = forest.predict(x_test)

        test_correct = 0
        for i in range(len(y_test)):
            classif = y_test[i]
            prediction = predictions[i]
            if classif == prediction:
                test_correct += 1
        
        folds_correct_avg += test_correct/len(x_test)
    correct_percent.append(folds_correct_avg/5)

plt.style.use('bmh')
plt.plot(num_trees, correct_percent)
plt.xlabel('num trees')
plt.ylabel('5-fold accuracy')
plt.savefig('sklearn_random_forest.png')
'''
# making data plot
plt.style.use('bmh')
points_list = point_dict_to_lists(points)
train_x = points_list[0]
train_points_x = [point[0] for point in train_x]
train_points_y = [point[1] for point in train_x]
train_classifs = points_list[1]
classif_colors = ['red' if classif==1 else '#00bfff' for classif in train_classifs]
for i in range(len(train_points_x)):
    plt.scatter(train_points_x[i], train_points_y[i], c=classif_colors[i])
tree = RandomForestClassifier(n_estimators=100)
tree.fit(train_x, train_classifs)

predict_vals = [i*0.1 for i in range(-10, 61)]
predict_points = [[i,j] for i in predict_vals for j in predict_vals]
predict_points_x = [point[0] for point in predict_points]
predict_points_y = [point[1] for point in predict_points]
predictions = tree.predict(predict_points)
predict_colors = ['red' if classif==1 else '#00bfff' for classif in predictions]
print("finished predictions")
for i in range(len(predict_points_x)):
    plt.scatter(predict_points_x[i], predict_points_y[i], c=predict_colors[i], s=5)
    print(i)
print('finished plotting')
plt.savefig('sklearn_forest_scatter_plot.png')
