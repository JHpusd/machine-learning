from enn_base import *
from numpy.random import normal as N

class EvolvingNeuralNet():
    def __init__(self, data, num_nets, act_func, node_layers, weight_range, mutat_rate):

        self.data = data
        self.num_nets = num_nets
        self.act_func = act_func
        self.node_layers = node_layers
        self.weight_range = weight_range
        self.mutat_rate = mutat_rate

        self.gen = 1

        self.nets = [RandomNeuralNet(node_layers,act_func,weight_range,mutat_rate) for _ in range(num_nets)]

    def set_rss(self, neural_net):
        rss = 0
        for x,y in self.data: 
            prediction = neural_net.predict(x)
            rss += (y - prediction)**2
        neural_net.rss = rss
        return rss
    
    def rss_all(self):
        for net in self.nets:
            self.set_rss(net)
    
    def avg_rss(self):
        self.rss_all()
        total = 0
        for net in self.nets:
            total += net.rss
        return total/len(self.nets)
    
    def avg_predict(self, x):
        result = 0
        for net in self.nets:
            result += net.predict(x)
        return result/len(self.nets)

    def make_child(self, neural_net):
        p_mutat_rate = neural_net.mutat_rate
        W = len(neural_net.w)
        weird_coefficient = math.exp(N(0,1) / ((2**0.5)*(W**0.25)))
        c_mutat_rate = p_mutat_rate * weird_coefficient

        child = RandomNeuralNet(self.node_layers,self.act_func,self.weight_range,c_mutat_rate)

        new_weights = {}
        for key in neural_net.w:
            p_weight = neural_net.w[key]
            new_weights[key] = p_weight + p_mutat_rate * N(0,1)
        
        child.set_weights(new_weights)
        return child
    
    def make_new_gen(self):
        self.rss_all()
        self.nets.sort(key=lambda x: x.rss)
        assert self.nets[0].rss < self.nets[len(self.nets)-1].rss, 'bruh'

        parents = list(self.nets[:int(self.num_nets/2)])
        children = [self.make_child(parent) for parent in parents]
        new_gen = parents + children

        self.nets = new_gen
        self.gen += 1
        assert len(self.nets) == self.num_nets

    def make_n_gens(self, n):
        for _ in range(n):
            self.make_new_gen()
