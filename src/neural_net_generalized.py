import matplotlib.pyplot as plt
import math, random

class Node():
    def __init__(self, num, act_func):
        self.num = num
        self.info_from = []
        self.info_to = []
        self.input_val = None
        self.output_val = None
        self.bias = False
        self.dRSS = 0
        self.f = act_func
    
    def set_vals(self, input_val):
        self.input_val = input_val
        self.output_val = self.f(input_val)

class NeuralNet():
    def __init__(self, weights, act_func, init_in, bias_nums, normalize=False):
        nodes_str = ''
        for key in weights:
            nodes_str += key
        self.num_nodes = int(max(nodes_str))
        self.nodes = [Node(num + 1, act_func) for num in range(self.num_nodes)]
        self.w = weights

        self.points = init_in
        if normalize:
            self.points = self.normalize_data(self.points)

        self.bias_nodes = [node for node in self.nodes if node.num in bias_nums]
        for node in self.bias_nodes:
            node.bias = True

        self.connect_nodes()
    
    def normalize_data(self, data):
        x = [point[0] for point in data]
        y = [point[1] for point in data]
        return [(10*(point[0]-min(x)) / (max(x)-min(x)), 10*(point[1]-min(y)) / (max(y)-min(y))) for point in data]

    def get_node(self, node_num):
        if type(node_num) == str:
            node_num = int(node_num)
        for node in self.nodes:
            if node.num == node_num:
                return node
    
    def get_weight(self, node_1, node_2):
        try:
            return self.w[f'{node_1.num}{node_2.num}']
        except KeyError:
            try:
                return self.w[f'{node_2.num}{node_1.num}']
            except KeyError:
                print(f'failed weight with {node_1.num} and {node_2.num}')
                return None

    def connect_nodes(self):
        for key in self.w:
            nodes = [self.get_node(char) for char in key]
            nodes[0].info_to.append(nodes[1])
            nodes[1].info_from.append(nodes[0])

    def set_node_vals(self, x):
        for node in self.nodes:
            if node.bias:
                node.output_val = 1
                continue
            if node.num == 1:
                node.set_vals(x)
                continue
            in_val = 0
            for in_node in node.info_from:
                edge_weight = self.get_weight(in_node, node)
                in_val += edge_weight * in_node.output_val
            node.set_vals(in_val)
    
    def predict(self, x):
        self.set_node_vals(x)
        return self.nodes[self.num_nodes-1].output_val
    
    def set_node_dRSS(self, point, f_prime): # can't generalize f_prime
        self.set_node_vals(point[0])
        for node in self.nodes[::-1]:
            node.dRSS = 0
            if node.num == self.num_nodes:
                node.dRSS = 2 * (node.output_val - point[1])
                continue
            for out_node in node.info_to:
                edge_weight = self.get_weight(node, out_node)
                node.dRSS += out_node.dRSS * f_prime(out_node.input_val) * edge_weight

    def weight_gradients(self, f_prime):
        gradients = {key:0 for key in self.w}
        for key in self.w:
            for point in self.points:
                self.set_node_dRSS(point, f_prime)
                nodes = [self.get_node(char) for char in key]
                gradients[key] += nodes[1].dRSS * f_prime(nodes[1].input_val) * nodes[0].output_val
        return gradients

    def rss(self):
        rss = 0
        for point in self.points:
            output = self.predict(point[0])
            rss += (output - point[1])**2
        return rss
    
    def gradient_desc(self, num_iterations, l_rate, f_prime):
        for _ in range(num_iterations):
            gradients = self.weight_gradients(f_prime)
            self.w = {key:self.w[key] - l_rate*gradients[key] for key in self.w}

'''
weights = {'13':1,'14':1,'23':1,'24':1,'36':1,'37':1,'46':1,'47':1,'56':1,'57':1,'69':1,'79':1,'89':1}
act_func = lambda x: 2*x
init_input = [(3,4)]
bias_nums = [2, 5, 8]
net = NeuralNet(9, weights, act_func, init_input, bias_nums)
net.set_node_dRSS((3,4), lambda x: 2)

n = net.nodes
print(n[0].dRSS)
#print(net.rss())
#net.gradient_desc(10000, 0.000001, lambda x: 2)
#print(net.rss())

weight_keys = ['13','14','23','24','36','37','46','47','56','57','69','79','89']
weights = {}
for key in weight_keys:
    weights[key] = 0.1*random.randint(-10,10)

act_func = lambda x: max(0,x)
init_input = [(-5,-3),(-4,-1),(-3,1),(-2,2),(-1,-1),(1,-1),(2,1),(3,2),(4,3),(5,4),(6,2),(7,0)]
bias_nums = [2, 5, 8]
f_prime = lambda x: 1 if x>0 else 0

net = NeuralNet(weights, act_func, init_input, bias_nums, normalize=True)
init_input = net.normalize_data(init_input)

plt.style.use('bmh')
plt.figure(0)
plt.scatter([point[0] for point in init_input], [point[1] for point in init_input], label='data')
x = [i*0.01 for i in range(0,1001)]
plt.plot(x,[net.predict(i) for i in x], label='unfit regressor')

num_iter = [1,2,5,10,15,25,35,50,75,100,150,200,300,500,1000,2000]
rss = []
for i in num_iter:
    net = NeuralNet({key:weights[key] for key in weights}, act_func, init_input, bias_nums)
    net.gradient_desc(i, 0.001, f_prime)
    print(net.rss())
    rss.append(net.rss())

plt.plot(x,[net.predict(i) for i in x], label='fit regressor')
plt.legend(loc='best')
plt.savefig('backpropagation_regression_plot.png')

plt.figure(1)
plt.plot(num_iter, rss)
plt.xlabel('num iterations')
plt.ylabel('regressor rss')
plt.savefig('backpropagation_iterations_vs_rss.png')

# f(x) = 2x works, descends faster
# f(x) = 0.5*x works, descends slower
# f(x) = arctan(x) descends very slow, increased step size a lot (up to 10), min rss > 80
# f(x) = 1/(1+e^(-x)) same as arctan, min rss > 100
# f(x) = x^2 diverges
# f(x) = e^x diverges
# f(x) = e^(e^x) diverges
# f(x) = 1/x diverges
# f(x) = 1/(x^5) diverges
'''
w = ['13','14','15','23','24','25','37','38','47','48','57','58','67','68','710','810','910']
weights = {key:1 for key in w}
