import matplotlib.pyplot as plt

f = lambda x: max(0, x)
# w = {'13':1, '14':1, '23':1, '24':1, '36':1, '46':1, '56':1}
data = [(0,5), (2,3), (5,10)]

def f_prime(x):
    if x < 0:
        return 0
    if x > 0:
        return 1
    if x == 0:
        print("f prime of 0 is undefined")
        return None

def pred(w,x):
    i3 = w['23'] + w['13'] * f(x)
    i4 = w['24'] + w['14'] * f(x)
    return w['36'] * f(i3) + w['46'] * f(i4) + w['56']

def point(point_num, in_data, in_or_out):
    if point_num in ['2','5']:
        if in_or_out == 'in':
            print('bias nodes have no input')
            return None
        return 1
    if point_num == '1':
        return in_data[0]
    in_val = 0
    for key in list(w.keys()):
        if key[1] == point_num:
            in_val += point(key[0], in_data, 'out') * w[key]
    if in_or_out == 'in':
        return in_val
    return f(in_val)

def get_rss(w):
    rss = 0
    for x in data:
        rss += (pred(w,x[0])-x[1])**2
    return rss

def dRSS_dw36(w):
    rss = 0
    for x in data:
        rss += 2*(pred(w,x[0])-x[1])*f_prime(point('6',x,'in'))*point('3',x,'out')
    return rss

def dRSS_dw46(w):
    rss = 0
    for x in data:
        rss += 2*(pred(w,x[0])-x[1])*f_prime(point('6',x,'in'))*point('4',x,'out')
    return rss

def dRSS_dw56(w):
    rss = 0
    for x in data:
        rss += 2*(pred(w,x[0])-x[1])*f_prime(point('6',x,'in'))*point('5',x,'out')
    return rss

def dRSS_dw13(w):
    rss = 0
    for x in data:
        path = f_prime(point('6',x,'in'))*w['36']*f_prime(point('3',x,'in'))*point('1',x,'out')
        rss += 2*(pred(w,x[0])-x[1])*path
    return rss

def dRSS_dw14(w):
    rss = 0
    for x in data:
        path = f_prime(point('6',x,'in'))*w['46']*f_prime(point('4',x,'in'))*point('1',x,'out')
        rss += 2*(pred(w,x[0])-x[1])*path
    return rss

def dRSS_dw23(w):
    rss = 0
    for x in data:
        path = f_prime(point('6',x,'in'))*w['36']*f_prime(point('3',x,'in'))*point('2',x,'out')
        rss += 2*(pred(w,x[0])-x[1])*path
    return rss

def dRSS_dw24(w):
    rss = 0
    for x in data:
        path = f_prime(point('6',x,'in'))*w['46']*f_prime(point('4',x,'in'))*point('2',x,'out')
        rss += 2*(pred(w,x[0])-x[1])*path
    return rss

def dRSS_dw(w,w_key):
    if w_key=='36':
        return dRSS_dw36(w)
    if w_key=='46':
        return dRSS_dw46(w)
    if w_key=='56':
        return dRSS_dw56(w)
    if w_key=='13':
        return dRSS_dw13(w)
    if w_key=='14':
        return dRSS_dw14(w)
    if w_key=='23':
        return dRSS_dw23(w)
    if w_key=='24':
        return dRSS_dw24(w)
    print('something went wrong')


def gradient_desc(w, num_iterations, l_rate):
    # currently updateing edge weights at same time
    for _ in range(num_iterations):
        gradients = {key:dRSS_dw(w, key) for key in list(w.keys())}
        w = {key:w[key] - l_rate*gradients[key] for key in list(w.keys())}
    # print(f'rss at {num_iterations} iterations: {get_rss(w)}')
    return w

num_iter = [1,2,5,10,15,25,35,50,75,100,150,200,300,500,1000,2000]
rss = []
test = True
for i in num_iter:
    w = {'13':1, '14':1, '23':1, '24':1, '36':1, '46':1, '56':1}
    w = gradient_desc(w, i, 0.0001)
    if i == 2 or i == 1:
        print(get_rss(w))
        test = False
    rss.append(get_rss(w))

plt.style.use('bmh')
plt.figure(0)
plt.plot(num_iter, rss)
plt.xlabel('num_iterations')
plt.ylabel('rss')
plt.savefig('num_iterations_vs_rss.png')

plt.figure(1)
w_default = {'13':1, '14':1, '23':1, '24':1, '36':1, '46':1, '56':1}
plt.scatter([point[0] for point in data], [point[1] for point in data],color='#2bc20e',label='data')

x_range = list(range(7))
w_default = {'13':1, '14':1, '23':1, '24':1, '36':1, '46':1, '56':1}
init = [pred(w_default,x) for x in x_range]
plt.plot(x_range, init, label='unfit regressor')

w_fitted = gradient_desc(w_default, 2000, 0.0001)
fitted = [pred(w_fitted,x) for x in x_range]
plt.plot(x_range, fitted, label='fitted regressor')

plt.legend(loc='best')
plt.savefig('regression_plot.png')