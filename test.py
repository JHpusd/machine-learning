import math, random as r
from numpy.random import normal as N
'''
def rss(func, points):
    rss = 0
    for point in points:
        x, y = point
        prediction = func(x)
        rss += (y - prediction)**2
    return rss

f = lambda x: 1.18 * (1.52 ** x)
points = [(2,3), (4,5), (6,18), (9,50)]

drrs_da = lambda points, a, b: sum([2*(a*b**x - y)*(b**x) for x,y in points])
drrs_db = lambda points, a, b: sum([2*(a*b**x - y)*(x*a*b**(x-1)) for x,y in points])

def gradient_desc(points, drrs_da, drrs_db, a, b, l_rate, steps):
    print(f'init rss: {rss(lambda x: a*b**x, points)}')
    for i in range(steps):
        a_new = a - drrs_da(points, a, b)*l_rate 
        b_new = b - drrs_db(points, a, b)*l_rate
        a = a_new
        b = b_new
    print(f'final rss: {rss(lambda x: a*b**x, points)}\n')
    return (a,b)

#print(gradient_desc(points, drrs_da, drrs_db, 1.1836141722222375, 1.5231327933344094, 0.0000001, 10000000))

# have l_rate * steps = 1 to have optimal rss

test = ['12', '34', '56']
weights = {key:(-1)**(int(key[0])+key[1]) * min(key[0],key[1]) / max(key[0], key[1]) for key in test}
#print(weights)
'''
print(1.0==1)