import random

def show_board(locations):
    for y in range(8):
        row_array = ['.', '.', '.', '.', '.', '.', '.', '.']
        for coord in locations:
            if coord[0] == y:
                row_array[coord[1]] = str(locations.index(coord))
        row_string = '  '.join(row_array)
        print(row_string)

locations = [(0,0), (6,1), (2,2), (5,3), (4,4), (7,5), (1,6), (2,6)]
'''
show_board(locations)
'''
def same_row(point_1, point_2):
    if point_1[0] == point_2[0]:
        return True
    else:
        return False

def same_col(point_1, point_2):
    if point_1[1] == point_2[1]:
        return True
    else:
        return False

def same_diag(point_1, point_2):
    delta_y = point_2[1] - point_1[1]
    delta_x = point_2[0] - point_1[0]
    if delta_y/delta_x == 1 or delta_y/delta_x == -1:
        return True
    else:
        return False

def calc_cost(locations):
    cost = 0
    for j in range(len(locations)):
        for i in range(len(locations)):
            if j == i:
                break
            if same_row(locations[j], locations[i]) or same_col(locations[j], locations[i]) or same_diag(locations[j], locations[i]):
                cost += 1
    return cost
'''
assert calc_cost(locations) == 10
'''
def random_optimizer(n):
    cost_dict = {}
    all_coords_list = []

    for _ in range(n):
        coord_list = []
        for _ in range(8):
            y_coord = random.randint(0,7)
            x_coord = random.randint(0,7)
            coord_list.append((y_coord, x_coord))
        all_coords_list.append(coord_list)

    lowest_cost = calc_cost(all_coords_list[0])
    lowest_cost_coords = all_coords_list[0]
    for coord_set in all_coords_list:
        if calc_cost(coord_set) < lowest_cost:
            lowest_cost = calc_cost(coord_set)
            lowest_cost_coords = coord_set
    cost_dict["locations"] = lowest_cost_coords
    cost_dict["cost"] = lowest_cost
    return cost_dict

print("n = 10:\n" + str(random_optimizer(10)) + "\n")
print("n = 50:\n" + str(random_optimizer(50)) + "\n")
print("n = 100:\n" + str(random_optimizer(100)) + "\n")
print("n = 500:\n" + str(random_optimizer(500)) + "\n")
print("n = 1000:\n" + str(random_optimizer(1000)))
