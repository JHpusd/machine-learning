import math as m
import random
#random.seed(1)

class DecisionTree():
    def __init__(self, point_dict, min_size_to_split):
        self.point_dict = point_dict
        self.entropy = self.get_entropy()
        self.parent = None
        self.branches = []
        self.set_split = None
        self.min_size = min_size_to_split
        self.random = False
    
    def get_all_coords(self, point_dict=None):
        result = []
        if point_dict == None:
            point_dict = self.point_dict
        for key in point_dict:
            result += point_dict[key]
        return result

    def get_entropy(self, point_dict=None):
        entropy = 0
        if point_dict == None:
            point_dict = self.point_dict
        for sign in point_dict:
            ratio = len(point_dict[sign])/len(self.get_all_coords(point_dict))
            if ratio == 0:
                continue
            entropy += -1*ratio*m.log(ratio)
        return entropy
    
    def remove_from_dict(self, input_dict, vals):
        copy_dict = input_dict.copy()
        if type(vals) is not list:
            vals = [vals]
        for key in copy_dict:
            items = list(copy_dict[key])
            new_items = [item for item in items if item not in vals]
            copy_dict[key] = new_items
        return copy_dict
    
    def get_midpoints(self, unique):
        midpoints = []
        for i in range(len(unique)-1):
            midpoints.append((unique[i]+unique[i+1])/2)
        return midpoints

    def get_splits(self, point_dict=None):
        result = []
        if point_dict == None:
            point_dict = self.point_dict
        all_coords = self.get_all_coords(point_dict)
        for i in range(len(all_coords[0])):
            unique = list(set([coord[i] for coord in all_coords]))
            midpoints = self.get_midpoints(unique)
            for midpoint in midpoints:
                result.append((i, midpoint))
        return result
    
    def split(self, split_tuple, point_dict=None):
        check = False
        if point_dict == None:
            check = True
            point_dict = self.point_dict
        index = split_tuple[0]
        val = split_tuple[1]
        greater = [coord for coord in self.get_all_coords(point_dict) if coord[index]>=val]
        lesser = [coord for coord in self.get_all_coords(point_dict) if coord[index]<val]
        greater_dict = self.remove_from_dict(point_dict, lesser)
        lesser_dict = self.remove_from_dict(point_dict, greater)
        if check:
            child_1 = DecisionTree(greater_dict,self.min_size)
            child_2 = DecisionTree(lesser_dict,self.min_size)
            child_1.parent = self
            child_2.parent = self
            self.branches = [child_1, child_2]
        return [greater_dict, lesser_dict]
    
    def weighted_entropy(self, point_dict_list):
        weighted_entropy = 0
        num_points = sum([len(self.get_all_coords(point_dict)) for point_dict in point_dict_list])
        for point_dict in point_dict_list:
            entropy = self.get_entropy(point_dict)
            num_point_ratio = len(self.get_all_coords(point_dict))/num_points
            weighted_entropy += entropy * num_point_ratio
        return weighted_entropy
    
    def get_best_split(self, point_dict=None):
        check = False
        if point_dict == None:
            check = True
            point_dict = self.point_dict
        all_splits = self.get_splits(point_dict)
        best_split = all_splits[0]
        best_entropy = self.weighted_entropy(self.split(best_split, point_dict))
        for split in all_splits:
            branches = self.split(split, point_dict)
            weighted_entropy = self.weighted_entropy(branches)
            if weighted_entropy < best_entropy:
                best_split = split
                best_entropy = weighted_entropy
        if check:
            self.set_split = best_split
        return best_split
    
    def get_random_split(self, point_dict=None):
        check = False
        if point_dict == None:
            check = True
            point_dict = self.point_dict
        all_splits = self.get_splits(point_dict)
        rand_split = all_splits[random.randint(0,len(all_splits)-1)]
        if check:
            self.set_split = rand_split
        return rand_split
    
    def fit(self, d_tree=None, random=False):
        if d_tree == None:
            d_tree = self
        if len(d_tree.branches) != 0 or len(d_tree.get_all_coords()) <= d_tree.min_size:
            return
        if random:
            d_tree.get_random_split()
            d_tree.random = True
        else:
            d_tree.get_best_split()
        d_tree.split(d_tree.set_split)
        branches = [branch for branch in d_tree.branches if branch.entropy != 0]
        next_branches = []
        while True:
            for branch in branches:
                if len(branch.get_all_coords()) <= branch.min_size or len(set(branch.get_all_coords()))==1:
                    continue
                if random:
                    branch.get_random_split()
                else:
                    branch.get_best_split()
                branch.split(branch.set_split)
                next_branches += [b for b in branch.branches if b.entropy != 0]
            branches = next_branches
            next_branches = []
            if len(branches) == 0:
                break
    
    def get_type(self, d_tree=None):
        if d_tree == None:
            d_tree = self
        if d_tree.entropy != 0:
            lengths = [(key,len(d_tree.point_dict[key])) for key in d_tree.point_dict]
            largest_len = max([pair[1] for pair in lengths])
            new_lengths = [pair for pair in lengths if pair[1]==largest_len]
            if len(new_lengths) > 1:
                r = random.randint(0,len(new_lengths)-1)
                return new_lengths[r][0]
            return new_lengths[0][0]
        target = [key for key in d_tree.point_dict.keys() if len(d_tree.point_dict[key]) != 0]
        return target[0]

    def predict(self, point, d_tree=None):
        if d_tree == None:
            d_tree = self
        d_tree.fit()
        while d_tree.entropy != 0 and len(d_tree.get_all_coords()) > d_tree.min_size and len(set(d_tree.get_all_coords()))!=1:
            i = d_tree.set_split[0]
            val = d_tree.set_split[1]
            if point[i] >= val:
                d_tree = d_tree.branches[0]
            elif point[i] < val:
                d_tree = d_tree.branches[1]
        return d_tree.get_type()