import random as r
import matplotlib.pyplot as plt
import math as m

x_clusters = [(1,1), (4,4)]
o_clusters = [(1,4), (4,1)]

def elem_add(a, b):
    assert len(a) == len(b), "different lengths"
    return [a[i]+b[i] for i in range(len(a))]

def generate_clusters(x_centers, o_centers, num_points):
    # num_points is number of extra points for each type
    # total number of added points will be num_points * 2
    if type(x_centers) != list:
        x_centers = [x_centers]
    if type(o_centers) != list:
        o_ceters = [o_centers]
    points = {'x':[], 'o':[]}

    pairs = [[pair[0], pair[1]] for pair in x_centers+o_centers]
    all_elems = []
    for pair in pairs:
        all_elems.append(pair[0])
        all_elems.append(pair[1])
    largest_dist = max(all_elems)
    # 60% chance to end up 0 to 1/4 of max
    # 25% chance to end up 1/4 to 1/2 of max
    # 10% chance to end up 1/2 to 3/4 of max
    # 5% chance to end up 3/4 to max
    weights = {60: (0,largest_dist/4), 85: (largest_dist/4,largest_dist/2), 95: (largest_dist/2, largest_dist*3/4), 100: (largest_dist*3/4, largest_dist)}

    for _ in range(num_points):
        x_center = x_centers[r.randint(0,len(x_centers)-1)]
        o_center = o_centers[r.randint(0,len(o_centers)-1)]

        for i in range(2):
            r_dist = r.randint(1,100)
            for key in weights:
                if r_dist <= key:
                    dist_range = weights[key]
                    break
            dist = r.randint(dist_range[0]*1000, dist_range[1]*1000) / 1000
            ang = m.pi*r.randint(0,360) / 180
            translation = (dist*m.cos(ang), dist*m.sin(ang))
            if i == 0:
                points['x'].append(elem_add(x_center, translation))
            elif i == 1:
                points['o'].append(elem_add(o_center, translation))
    
    return points

points = generate_clusters([(1,1), (4,4)], [(1,4), (4,1)], 100)
plt.style.use('bmh')
#print([p[0] for p in points['x']])
plt.scatter([p[0] for p in points['x']], [p[1] for p in points['x']], color='red',s=10, label='x')
plt.scatter([p[0] for p in points['o']], [p[1] for p in points['o']], color='#66ff00',s=10,label='o')
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.legend(loc='lower left')
plt.savefig('semirandom_clusters.png')