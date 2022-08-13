
class NaiveBayes():
    def __init__(self, data_dict):
        self.data = data_dict
        self.cols = list(data_dict.keys())
        self.col_vals = list(data_dict.values())
        col_lens = [(len(i) for i in self.col_vals)]
        assert len(set(col_lens)) == 1, 'col len error'
        self.num_rows = len(self.col_vals[0])
    
    def num_classes(self, column):
        col = self.data[column]
        return len(set(col))
    
    def prob(self, col_name, val):
        num_match = len([i for i in self.data[col_name] if i==val])
        return num_match/self.num_rows

    def cond_prob(self, col, val, given_col, given_val):
        num_given = 0
        num_match = 0
        for i in range(self.num_rows):
            check_row = False
            for key in self.cols:
                item = self.data[key][i]
                if key == given_col and item == given_val:
                    num_given += 1
                    check_row = True
            if check_row and self.data[col][i]==val:
                num_match += 1
        return num_match/num_given

    def predict(self, data_dict):
        input_cols = list(data_dict.keys())
        assert all(key in self.cols for key in input_cols), 'input data key error'
        input_len = len(data_dict[input_cols[0]])
        dep_var = [i for i in self.cols if i not in input_cols]
        assert len(dep_var) == 1, 'dependent variable error'
        dep_var = dep_var[0]

        result = []
        classifs = list(set(self.data[dep_var]))

        for i in range(input_len):
            compared_vals = []
            for classif in classifs:
                val = self.prob(dep_var, classif)
                for key in input_cols:
                    val *= self.cond_prob(key,data_dict[key][i],dep_var,classif)
                compared_vals.append(val)
            max_index = compared_vals.index(max(compared_vals)) # not accounting for ties
            result.append(classifs[max_index])
        
        return result
            