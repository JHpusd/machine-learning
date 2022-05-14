import math, random as r

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

class EvolvingNeuralNet():
    def __init__(self, node_layers, act_func, weight_range, mutat_rate, bias=True):
        # node layers gives number of non-bias nodes in each layer
        self.num_nodes = sum(node_layers)
        if bias and len(node_layers) > 2:
            self.num_nodes += len(node_layers) - 2

        self.nodes = [Node(num + 1, act_func) for num in range(self.num_nodes)]
        self.bias_nums = []

        self.w = self.random_weights(node_layers, bias, weight_range)

        self.bias_nodes = [node for node in self.nodes if node.num in self.bias_nums]
        for node in self.bias_nodes:
            node.bias = True
        
        self.mutat_rate = mutat_rate

        self.connect_nodes()
    
    def random_weights(self, node_layers, bias, weight_range):
        layer_rep = []
        counter = 1
        for i in range(len(node_layers)):
            num = node_layers[i]
            layer_rep.append([])
            if bias and i != 0 and i != len(node_layers)-1:
                num += 1
            for _ in range(num):
                layer_rep[i].append(str(counter))
                counter += 1

        weight_indicators = []
        for i in range(len(layer_rep)-1):
            layer = layer_rep[i]
            next_layer = layer_rep[i+1]
            if bias and i+1 != len(layer_rep) - 1:
                self.bias_nums.append(int(next_layer[-1]))
                next_layer = next_layer[:-1]

            for node_num_1 in layer:
                for node_num_2 in next_layer:
                    weight_indicators.append(node_num_1 + node_num_2)
        
        return {w:r.randrange(weight_range[0]*1000, weight_range[1]*1000)/1000 for w in weight_indicators}

    def get_node(self, node_num):
        if type(node_num) == str:
            node_num = int(node_num)
        for node in self.nodes:
            if node.num == node_num:
                return node
    
    def nodes_from_weight_str(self, weight_str):
        node_1_num = int(weight_str[:int(len(weight_str)/2)])
        node_2_num = int(weight_str[int(len(weight_str)/2):])
        return [self.get_node(node_1_num), self.get_node(node_2_num)]
    
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
            nodes = self.nodes_from_weight_str(key)
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
