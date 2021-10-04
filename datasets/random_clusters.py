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

    for _ in range(num_points):
        x_center = x_centers[r.randint(0,len(x_centers)-1)]
        o_center = o_centers[r.randint(0,len(o_centers)-1)]

        for i in range(2):
            dist_scalar = (r.randint(1,100)**3) / 1000000
            dist = largest_dist * dist_scalar
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