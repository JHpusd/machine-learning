import sys
sys.path.append('src')
from kmeans import *
import matplotlib.pyplot as plt

data = [[0.14, 0.14, 0.28, 0.44],
        [0.22, 0.1, 0.45, 0.33],
        [0.1, 0.19, 0.25, 0.4],
        [0.02, 0.08, 0.43, 0.45],
        [0.16, 0.08, 0.35, 0.3],
        [0.14, 0.17, 0.31, 0.38],
        [0.05, 0.14, 0.35, 0.5],
        [0.1, 0.21, 0.28, 0.44],
        [0.04, 0.08, 0.35, 0.47],
        [0.11, 0.13, 0.28, 0.45],
        [0.0, 0.07, 0.34, 0.65],
        [0.2, 0.05, 0.4, 0.37],
        [0.12, 0.15, 0.33, 0.45],
        [0.25, 0.1, 0.3, 0.35],
        [0.0, 0.1, 0.4, 0.5],
        [0.15, 0.2, 0.3, 0.37],
        [0.0, 0.13, 0.4, 0.49],
        [0.22, 0.07, 0.4, 0.38],
        [0.2, 0.18, 0.3, 0.4]]

columns = ['Portion Eggs','Portion Butter','Portion Sugar','Portion Flour']
'''
initial_clusters = {
    1: [0,3,6,9,12,15,18],
    2: [1,4,7,10,13,16],
    3: [2,5,8,11,14,17]
    }

kmeans = KMeans(initial_clusters, data)
kmeans.run()
print(kmeans.clusters)
'''
def make_clusters(k_val, data):
    clusters = {k:[] for k in range(1, k_val+1)}
    for i in range(len(data)):
        clusters[(i % k_val) + 1].append(i)
    return clusters

def list_squared_error(list_1, list_2):
    assert len(list_1) == len(list_2), "lists are different length"
    error = 0
    for i in range(len(list_1)):
        error += (list_1[i] - list_2[i])**2
    return error

def squared_error(completed_kmeans):
    clusters = completed_kmeans.clusters
    data = completed_kmeans.data
    centers = completed_kmeans.centers
    total_error = 0
    for key in clusters:
        center = centers[key]
        data_indices = clusters[key]
        for index in data_indices:
            row = data[index]
            total_error += list_squared_error(center, row)
    return total_error

k = [1,2,3,4,5]
errors = []
for k_val in k:
    clusters = make_clusters(k_val, data)
    kmeans = KMeans(clusters, data)
    kmeans.run()
    errors.append(squared_error(kmeans))
plt.style.use('bmh')
plt.plot(k, errors)
plt.xlabel('k')
plt.xticks(k)
plt.ylabel('sum squared error')
plt.ylim(0, 0.4)
plt.savefig('kmeans_clustering_elbow_method.png')
print("Best number of clusters is 3")

