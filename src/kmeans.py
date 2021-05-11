import math

class KMeans():
    def __init__(self, init_clusters, data):
        self.clusters = init_clusters
        self.data = data
        self.centers = {n:self.get_centers(self.clusters[n]) for n in self.clusters}
    
    def list_element_add(self, list1, list2):
        assert len(list1) == len(list2), "cannot element add lists of different lengths"
        return [list1[i]+list2[i] for i in range(len(list1))]
    
    def get_centers(self, data_indices):
        total = self.data[data_indices[0]]
        for index in data_indices[1:]:
            data_row = self.data[index]
            total = self.list_element_add(total, data_row)
        return [val / len(data_indices) for val in total]
    
    def reset_centers(self):
        self.centers = {n:self.get_centers(self.clusters[n]) for n in self.clusters}
    
    def find_distance(self, item_1, item_2):
        sum_of_squares = 0
        assert len(item_1) == len(item_2)
        for i in range(len(item_1)):
            sum_of_squares += (item_1[i] - item_2[i])**2
        return math.sqrt(sum_of_squares)
    
    def find_nearest_center(self, data_index):
        row = self.data[data_index]
        smallest_center_key = list(self.centers.items())[0][0]
        smallest_distance = self.find_distance(row, self.centers[smallest_center_key])
        for key in self.centers:
            if self.find_distance(row, self.centers[key]) < smallest_distance:
                smallest_center_key = key
                smallest_distance = self.find_distance(row, self.centers[key])
        return smallest_center_key
    
    def reset_clusters(self):
        new_clusters = {n:[] for n in self.clusters}
        for i in range(len(self.data)):
            new_clusters[self.find_nearest_center(i)].append(i)
        if new_clusters == self.clusters:
            return True
        self.clusters = new_clusters
        return False
    
    def update_once(self):
        self.reset_centers()
        self.reset_clusters()
    
    def run(self):
        while True:
            self.reset_centers()
            if self.reset_clusters():
                break
