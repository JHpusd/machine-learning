import sys
sys.path.append('src')
from decision_tree import *

class Forest():
    def __init__(self, num_trees, training_point_dict, min_size_to_split):
        self.num_trees = num_trees
        self.training = training_point_dict
        self.min_size = min_size_to_split
        self.trees = []
    
    def init_trees(self):
        self.trees = [DecisionTree(self.training, self.min_size) for _ in range(self.num_trees)]
    
    def fit_trees(self, r=True):
        for tree in self.trees:
            tree.fit(random=r)
    
    def predict(self, point):
        classifs = {key:0 for key in self.training}
        for tree in self.trees:
            classifs[tree.predict(point)] += 1
        
        best_key = list(classifs.keys())[0]
        most_classifs = classifs[best_key]
        for key in classifs:
            if classifs[key] > most_classifs:
                best_key = key
                most_classifs = classifs[key]
        
        ties = [key for key in classifs if classifs[key]==most_classifs]
        return ties[random.randint(0,len(ties)-1)]