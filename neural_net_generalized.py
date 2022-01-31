import matplotlib.pyplot as plt

class Node():
    def __init__(self, num, act_func):
        self.num = num
        self.info_from = []
        self.info_to = []
        self.input_val = None
        self.output_val = None
        self.bias = False
        self.dRSS = None
        self.f = act_func
    
    def set_vals(self, input_val):
        self.input_val = input_val
        self.output_val = self.f(input_val)

class NeuralNet():
    def __init__(self, num_nodes, weights, act_func, init_in, bias_nums):
        self.num_nodes = num_nodes
        self.nodes = [Node(num + 1, act_func) for num in range(num_nodes)]
        self.points = init_in
        self.w = weights

        self.bias_nodes = [node for node in self.nodes if node.num in bias_nums]
        for node in self.bias_nodes:
            node.bias = True
        
        self.connect_nodes()

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
    
    def set_node_dRSS(self, f_prime): # can't generalize f_prime
        for node in self.nodes[::-1]:
            drss = 0
            for point in self.points:
                self.set_node_vals(point[0])
                if node.num == self.num_nodes:
                    drss += 2 * (node.output_val - point[1])
                    continue
                for out_node in node.info_to:
                    edge_weight = self.get_weight(node, out_node)
                    drss += out_node.dRSS * f_prime(out_node.input_val) * edge_weight
            node.dRSS = drss

    def weight_gradients(self, f_prime):
        gradients = {key:0 for key in self.w}
        for key in self.w:
            for point in self.points:
                self.set_node_vals(point[0])
                nodes = [self.get_node(char) for char in key]
                gradients[key] += nodes[1].dRSS * f_prime(nodes[1].input_val) * nodes[0].output_val
        return gradients

    def rss(self):
        rss = 0
        for point in self.points:
            self.set_node_vals(point[0])
            output = self.nodes[self.num_nodes-1].output_val
            rss += (output - point[1])**2
        return rss
    
    def gradient_desc(self, num_iterations, l_rate, f_prime):
        for _ in range(num_iterations):
            self.set_node_dRSS(f_prime)
            gradients = self.weight_gradients(f_prime)
            self.w = {key:self.w[key] - l_rate*gradients[key] for key in self.w}
'''
weights = {'13':1,'14':1,'23':1,'24':1,'36':1,'37':1,'46':1,'47':1,'56':1,'57':1,'69':1,'79':1,'89':1}
act_func = lambda x: 2*x
init_input = [(3,4)]
bias_nums = [2, 5, 8]
net = NeuralNet(9, weights, act_func, init_input, bias_nums)
print(net.rss())
net.gradient_desc(10000, 0.000001, lambda x: 2)
print(net.rss())
'''
weights = {'13':1,'14':1,'23':1,'24':1,'36':1,'46':1,'56':1}
act_func = lambda x: max(0,x)
init_input = [(0,5), (2,3), (5,10)]
bias_nums = [2, 5]
f_prime = lambda x: x
net = NeuralNet(6, {key:weights[key] for key in weights}, act_func, init_input, bias_nums) # the copy method cannot be trusted

plt.style.use('bmh')
plt.figure(0)
plt.scatter([point[0] for point in init_input], [point[1] for point in init_input], label='data')
x = [i for i in range(0,6)]
plt.plot(x,[net.predict(i) for i in x], label='unfit regressor')

num_iter = [1,2,5,10,15,25,35,50,75,100,150,200]
rss = []
for i in num_iter:
    net = NeuralNet(6, dict(weights), act_func, init_input, bias_nums)
    net.gradient_desc(i, 0.0001, f_prime)
    rss.append(net.rss())

plt.plot(x,[net.predict(i) for i in x], label='fit regressor')
plt.legend(loc='best')
plt.savefig('backpropagation_regression_plot.png')

plt.figure(1)
plt.plot(num_iter, rss)
plt.xlabel('num iterations')
plt.ylabel('regressor rss')
plt.savefig('backpropagation_iterations_vs_rss.png')