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

data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}

print("Testing class DataFrame ...")
df1 = DataFrame(data_dict, ['Pete', 'John', 'Sarah'])

assert df1.data_dict == {'Pete': [1, 0, 1, 0],'John': [2, 1, 0, 2],'Sarah': [3, 1, 4, 0]}
assert df1.columns == ['Pete', 'John', 'Sarah']
assert df1.to_array() == [[1, 2, 3], [0, 1, 1], [1, 0, 4], [0, 2, 0]]

df2 = df1.select_columns(['Sarah', 'Pete'])
assert df2.to_array() == [[3, 1], [1, 0], [4, 1], [0, 0]]
assert df2.columns == ['Sarah', 'Pete']

df3 = df1.select_rows([1, 3])
assert df3.to_array() == [[0, 1, 1], [0, 2, 0]]
print("PASSED")
