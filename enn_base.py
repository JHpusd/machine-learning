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

class RandomNeuralNet():
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

        self.rss = None # for evolving neural net algorithm
    
    def set_weights(self, new_weights):
        self.w = new_weights
    
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

def tanh(x):
    top = math.exp(x) - math.exp(-x)
    bottom = math.exp(x) + math.exp(-x)
    return top/bottom
