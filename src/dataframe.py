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
    
    @classmethod
    def from_csv(cls, pathing, header):
        data = {}
        col_names = []
        with open(pathing, "r") as file:
            full_split_file = []
            file_rows = file.read().split('\n')
            for row in file_rows:
                full_split_file.append(row.split(', '))
        if header == True:
            for element in full_split_file[0]:
                col_names.append(element)
        elif header == False:
            for i in range(len(full_split_file[0])):
                col_names.append(i)
        for i in range(len(col_names)):
            data[col_names[i]] = []
            for j in range(len(full_split_file)):
                data[col_names[i]].append(full_split_file[j][i])
        for key in data:
            data[key] = data[key][1:]
        return cls(data, col_names)
    
    def create_interaction_terms(self, col_1, col_2):
        new_data_dict = {}
        for key in self.data_dict:
            new_data_dict[key] = self.data_dict[key]
        new_cols = [col for col in self.columns]
        new_cols.append(col_1 + ' * ' + col_2)
        col_1_list = self.data_dict[col_1]
        col_2_list = self.data_dict[col_2]
        new_col_list = [col_1_list[i]*col_2_list[i] for i in range(len(col_1_list))]
        new_data_dict[col_1 + ' * ' + col_2] = new_col_list
        return DataFrame(new_data_dict, new_cols)

    def create_dummy_variables(self, dummy_name):
        target_row = [i for i in self.data_dict[dummy_name]]

        dummy_vars = []
        for i in target_row:
            for var in i:
                if var not in dummy_vars:
                    dummy_vars.append(var)

        new_cols = []
        for col_name in self.columns:
            if col_name != dummy_name:
                new_cols.append(col_name)
            else:
                for var_name in dummy_vars:
                    new_cols.append(var_name)

        new_data_dict = {key:self.data_dict[key] for key in self.data_dict}
        del new_data_dict[dummy_name]
        for var in dummy_vars:
            new_data_dict[var] = [0 if var not in i else 1 for i in target_row]
        
        return DataFrame(new_data_dict, new_cols)

