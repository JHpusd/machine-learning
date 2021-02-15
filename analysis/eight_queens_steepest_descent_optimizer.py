import sys
import random
sys.path.append('analysis')
from eight_queens import *

def steepest_descent_optimizer(n):
    init_dict = random_optimizer(100)
    print("n = " + str(n) + ":\ninitial dictionary: " + str(init_dict))
    init_loc = init_dict['locations']
    init_cost = init_dict['cost']
    for _ in range(n):
        for coord_index in range(len(init_loc)):
            adjacent = []
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    adjacent.append((init_loc[coord_index][0]+i, init_loc[coord_index][1]+j))
            for adj_coord in adjacent:
                if not 0<=adj_coord[0]<=7 or not 0<=adj_coord[1]<=7:
                    adjacent.remove(adj_coord)
                    continue
                if adj_coord in init_loc:
                    adjacent.remove(adj_coord)
                    continue
                new_loc = [loc for loc in init_loc]
                new_loc[coord_index] = adj_coord
                if calc_cost(new_loc) < init_cost:
                    init_loc = new_loc
                    init_cost = calc_cost(new_loc)
    return {'locations':init_loc, 'cost':init_cost}

print("optimized dictionary: " + str(steepest_descent_optimizer(10)) + "\n")
print("optimized dictionary: " + str(steepest_descent_optimizer(50)) + "\n")
print("optimized dictionary: " + str(steepest_descent_optimizer(100)) + "\n")
print("optimized dictionary: " + str(steepest_descent_optimizer(500)) + "\n")
print("optimized dictionary: " + str(steepest_descent_optimizer(1000)))


