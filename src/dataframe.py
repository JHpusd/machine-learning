class DataFrame():
    def __init__(self, input_dict, column_order):
        self.data_dict = input_dict
        self.columns = column_order
    
    def to_array(self):
        result = []
        counter = 0
        for j in range(len(self.data_dict[self.columns[0]])):
            result.append([])
            for key in self.columns:
                result[counter].append(self.data_dict[key][j])
            counter += 1
        return result
    
    def select_columns(self, column_order):
        return DataFrame(self.data_dict, column_order)
    
    def select_rows(self, row_order):
        clone_dict = self.data_dict
        for key in self.columns:
            new_list = []
            for j in range(len(clone_dict[key])):
                if j in row_order:
                    new_list.append(clone_dict[key][j])
            clone_dict[key] = new_list
        return DataFrame(clone_dict, self.columns)
    
    def apply(self, key, function):
        new_list = []
        for num in self.data_dict[key]:
            new_list.append(function(num))
        self.data_dict[key] = new_list
        return self
