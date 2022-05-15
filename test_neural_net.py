from evolving_neural_net import *
import matplotlib.pyplot as plt

def normalize_data(data):
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    return [((point[0]-min(x)) / (max(x)-min(x)), (2*(point[1]-min(y)) / (max(y)-min(y)))-1) for point in data]

data = [(0.0 , 7) , (0.2 , 5.6) , (0.4 , 3.56) , (0.6 , 1.23) , (0.8 , -1.03) ,
 (1.0 , -2.89) , (1.2 , -4.06) , (1.4 , -4.39) , (1.6 , -3.88) , (1.8 , -2.64) ,
 (2.0 , -0.92) , (2.2 , 0.95) , (2.4 , 2.63) , (2.6 , 3.79) , (2.8 , 4.22) ,
 (3.0 , 3.8) , (3.2 , 2.56) , (3.4 , 0.68) , (3.6 , -1.58) , (3.8 , -3.84) ,
 (4.0 , -5.76) , (4.2 , -7.01) , (4.4 , -7.38) , (4.6 , -6.76) , (4.8 , -5.22) ]
data = normalize_data(data)

num_nets = 30

def tanh(x):
    top = math.exp(x) - math.exp(-x)
    bottom = math.exp(x) + math.exp(-x)
    return top/bottom

node_layers = [1,10,6,3,1]
weight_range = [-0.2, 0.2]
mutat_rate = 0.05

enn = EvolvingNeuralNet(data, num_nets, tanh, node_layers, weight_range, mutat_rate)

graph_x = [x/1000 for x in range(0, 1200)]

plt.style.use('bmh')
plt.figure(0)
plt.scatter([p[0] for p in data], [p[1] for p in data])
for net in enn.nets:
    plt.plot(graph_x, [net.predict(x) for x in graph_x], color='red', alpha=0.65)

gens = [1,2,5,10,15,20,25,50,100,150,200,250,500,750,1000,1500,2000,2500,3000]
avg_rss = []
for num in gens:
    while enn.gen != num:
        enn.make_new_gen()
    avg_rss.append(enn.avg_rss())

for net in enn.nets:
    plt.plot(graph_x, [net.predict(x) for x in graph_x], color='#138a07', alpha=0.5)
plt.savefig('enn_init_and_final_regressions.png')

plt.figure(1)
plt.plot(gens, avg_rss)
plt.xlabel('generation')
plt.ylabel('average rss')
plt.savefig('enn_gen_vs_average_rss.png')
