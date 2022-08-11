from neural_net_generalized import *

data = [(1,2),(3,4)]

def f(x):
    return x

def f_p(x):
    return 1

weights = {'12':1,'13':1,'24':1,'25':1,'34':1,'35':1,'46':1,'56':1}
bias_nums = []

nn = NeuralNet(weights, f, data, bias_nums)
print(nn.weight_gradients(f_p))
print([node.dRSS for node in nn.nodes])