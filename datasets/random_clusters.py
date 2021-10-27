import random as r
import matplotlib.pyplot as plt
import math as m

x_clusters = [(1,1), (4,4)]
o_clusters = [(1,4), (4,1)]

def elem_add(a, b):
    assert len(a) == len(b), "different lengths"
    elems = [a[i]+b[i] for i in range(len(a))]
    return tuple(elems)

def generate_clusters(x_centers, o_centers, p, max_dist, num_points):
    # num_points is number of extra points for each type
    # total number of added points will be num_points * 2
    if type(x_centers) != list:
        x_centers = [x_centers]
    if type(o_centers) != list:
        o_ceters = [o_centers]
    points = {1:[], 2:[]}

    for _ in range(num_points):
        x_center = x_centers[r.randint(0,len(x_centers)-1)]
        o_center = o_centers[r.randint(0,len(o_centers)-1)]

        for i in range(2):
            dist_scalar = (r.randint(1,100)**p) / 100**p
            dist = max_dist * dist_scalar
            ang = m.pi*r.randint(0,360) / 180
            translation = (dist*m.cos(ang), dist*m.sin(ang))
            if i == 0:
                points[1].append(elem_add(x_center, translation))
            elif i == 1:
                points[2].append(elem_add(o_center, translation))
    
    return points

def show(point_dict, x_lim=None, y_lim=None, filename='semirandom_clusters'):
    plt.style.use('bmh')
    plt.clf()
    for key in point_dict:
        plt.scatter([p[0] for p in point_dict[key]], [p[1] for p in point_dict[key]],marker=key,s=20)
    if x_lim != None:
        plt.xlim(x_lim[0], x_lim[1])
    if y_lim != None:
        plt.ylim(y_lim[0], y_lim[1])
    plt.savefig(filename+'.png')

#points = generate_clusters(x_clusters, o_clusters, 2, 4, 100)
#show(points, (-8,8), (-8,8))