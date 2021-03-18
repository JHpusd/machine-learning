import sys
sys.path.append('src')
from dataframe import DataFrame
from matrix import Matrix

class LinearRegressor():
    def __init__(self, data, dependent_variable):
        self.df = data
        self.dv = dependent_variable
        self.coefficients = self.calculate_coefficients()
    
    def calculate_coefficients(self):
        df_array = self.df.to_array()
        d_index = self.df.columns.index(self.dv)
        d_column = []
        for i in range(len(df_array)):
            d_column.append([])
            d_column[i].append(df_array[i][d_index])
        d_column = Matrix(d_column)
        sys_eq_matrix = []
        for i in range(len(df_array)):
            sys_eq_matrix.append([1])
            for j in range(len(df_array[0])):
                if j != d_index:
                    sys_eq_matrix[i].append(df_array[i][j])
        sys_matrix = Matrix(sys_eq_matrix)
        trans_sys_matrix = sys_matrix.transpose()
        inv_sys_matrix = (trans_sys_matrix @ sys_matrix).inverse()
        coeff_matrix = inv_sys_matrix @ trans_sys_matrix @ d_column
        coeff_dict = {'constant':coeff_matrix.elements[i][0]}
        no_dv_columns = [col for col in self.df.columns]
        no_dv_columns.remove(self.dv)
        for i in range(1, len(no_dv_columns) + 1):
            coeff_dict[no_dv_columns[i-1]] = coeff_matrix.elements[i][0]
        return coeff_dict

    def predict(self, input_dict):
        all_cols = [col for col in self.df.columns]
        all_cols.remove(self.dv)
        
        for key in all_cols:
            if key not in input_dict and " * " not in key:
                input_dict[key] = 0
            if key not in input_dict and " * " in key:
                keys = key.split(" * ")
                input_dict[key] = input_dict[keys[0]] * input_dict[keys[1]]

        result = 0
        for key in self.coefficients:
            if key in input_dict:
                result += self.coefficients[key] * input_dict[key]
            elif key not in input_dict:
                result += self.coefficients[key]
        return result
    


