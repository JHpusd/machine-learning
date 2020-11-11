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
    
    @classmethod
    def from_array(cls, arr, columns):
        new_dict = {}
        for i in range(len(columns)):
            new_dict[columns[i]] = []
            for j in range(len(arr)):
                new_dict[columns[i]].append(arr[j][i])
        return cls(new_dict, columns)
    
    def convert_row_from_array_to_dict(self, row, columns):
        result_dict = {}
        for i in range(len(columns)):
            result_dict[columns[i]] = row[i]
        return result_dict
    
    def select_rows_where(self, function):
        array_copy = self.to_array()
        result_list = []
        for data_row in array_copy:
            row_dict = self.convert_row_from_array_to_dict(data_row, self.columns)
            if function(row_dict):
                result_list.append(data_row)
            else:
                continue
        return DataFrame.from_array(result_list, self.columns)
    
    def order_by(self, attribute, ascent):
        array_copy = self.to_array()
        att_index = self.columns.index(attribute)
        result_list = []
        while len(array_copy) > 0:
            min_row = array_copy[0]
            for data_row in array_copy:
                if data_row[att_index] < min_row[att_index]:
                    min_row = data_row
            result_list.append(min_row)
            array_copy.remove(min_row)
        if ascent:
            return DataFrame.from_array(result_list, self.columns)
        else:
            return DataFrame.from_array(result_list[::-1], self.columns)
