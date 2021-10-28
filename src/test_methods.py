import math as m
import random

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
        r_key = keys[random.randint(0,len(keys)-1)]
        if len(point_dict[r_key]) == 0:
            keys.remove(r_key)
            r_key = keys[random.randint(0,len(keys)-1)]
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

def correct_percent(fitted_classifier, test_point_dict):
    total = 0
    correct = 0
    for key in test_point_dict:
        for coord in test_point_dict[key]:
            if fitted_classifier.predict(coord) == key:
                correct += 1
            total += 1
    return correct / total

def get_training(all_folds, excluded_fold):
    point_dict_list = [fold for fold in all_folds if fold != excluded_fold]
    return add_point_dicts(point_dict_list)

def get_percent(percent_decimal, point_dict):
    assert percent_decimal <= 1, "percent needs to be decimal"
    size = round(len(get_all_vals(point_dict)) * percent_decimal)
    return random_fold(point_dict, size)

def point_dict_to_lists(point_dict):
    y = []
    x = []
    for key in list(point_dict.keys()):
        for pair in point_dict[key]:
            y.append(key)
            x.append(list(pair))
    return (x,y)

