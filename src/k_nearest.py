import math
import pandas as pd
import numpy as np

class KNearestNeighborsClassifier():
    def __init__(self, k):
        self.k = k
    
    def fit(self, dataframe, dependent_var):
        self.df = dataframe
        self.cols = dataframe.columns
        self.dv = dependent_var
    
    def compute_distances(self, observation):
        copy_cols = [col for col in self.cols if col != self.dv]
        df_copy = self.df[copy_cols]

        distance_list = []
        for i in range(len(list(df_copy[df_copy.columns[0]]))):
            distance = 0
            for col in observation:
                obs_val = float(observation[col])
                df_val = float(df_copy[col][i])
                distance += (obs_val - df_val) ** 2
            distance_list.append(math.sqrt(distance))

        distance_df = {}
        distance_df['Distance'] = distance_list
        distance_df[self.dv] = [dv for dv in list(self.df[self.dv])]
        return pd.DataFrame.from_dict(distance_df)
    
    def nearest_neighbors(self, observation):
        distance_df = self.compute_distances(observation)
        distance_index = distance_df.columns.tolist().index('Distance')
        distance_df_arr = distance_df.to_numpy().tolist()
        
        new_df_arr = []
        while len(distance_df_arr) != 0:
            smallest_dist = distance_df_arr[0][distance_index]
            smallest_dist_row = distance_df_arr[0]
            for row in distance_df_arr:
                if row[distance_index] < smallest_dist:
                    smallest_dist = row[distance_index]
                    smallest_dist_row = row
            new_df_arr.append(smallest_dist_row)
            distance_df_arr.remove(smallest_dist_row)
        return pd.DataFrame(np.array(new_df_arr), columns=distance_df.columns.tolist())

    def get_classification(self, count_and_avg):
        best_key = list(count_and_avg.keys())[0]
        largest_count = count_and_avg[best_key][0]
        smallest_avg = count_and_avg[best_key][1]

        for key in count_and_avg:
            if count_and_avg[key][0] > largest_count:
                best_key = key
                largest_count = count_and_avg[key][0]
                smallest_avg = count_and_avg[key][1]
            elif count_and_avg[key][0] == largest_count:
                if count_and_avg[key][1] < smallest_avg:
                    best_key = key
                    largest_count = count_and_avg[key][0]
                    smallest_avg = count_and_avg[key][1]
        return best_key

    def classify(self, observation):
        distance_df = self.nearest_neighbors(observation)
        distance_index = distance_df.columns.tolist().index('Distance')
        dv_index = distance_df.columns.tolist().index(self.dv)
        distance_df_arr = distance_df.to_numpy().tolist()[:self.k]
        
        count_and_avg = {}
        for row in distance_df_arr:
            if row[dv_index] in count_and_avg:
                count_and_avg[row[dv_index]][0] += 1
                count_and_avg[row[dv_index]][1] += float(row[distance_index])
            else:
                count_and_avg[row[dv_index]] = [1, float(row[distance_index])]
        for key in count_and_avg:
            count_and_avg[key][1] /= count_and_avg[key][0]
        return self.get_classification(count_and_avg)

    def leave_one_out_true_false(self, row_index):
        print("k="+str(self.k)+", leave_out_index="+str(row_index)+": ",end="")
        copy_cols = [col for col in self.cols if col != self.dv]
        df_copy = self.df[copy_cols]

        classification = self.df[self.dv].iloc[[row_index]].to_numpy().tolist()[0]
        values = df_copy.iloc[[row_index]].to_numpy().tolist()[0]
        observation = {copy_cols[i]:values[i] for i in range(len(copy_cols))}

        fitting_df = self.df.drop([row_index])
        fitting_df = fitting_df.reset_index(drop=True)
        dummy_knn = KNearestNeighborsClassifier(self.k)
        dummy_knn.fit(fitting_df, self.dv)
        result_classification = dummy_knn.classify(observation)
        
        if result_classification == classification:
            print("correct")
            return True
        print("incorrect")
        return False

    def leave_one_out_accuracy(self):
        df_arr = self.df.to_numpy().tolist()
        correct = 0
        for row_index in range(len(df_arr)):
            if self.leave_one_out_true_false(row_index):
                correct += 1
        return correct / len(df_arr)

