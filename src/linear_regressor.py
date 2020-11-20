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
            sys_eq_matrix.append([])
            for j in range(len(df_array[0])):
                if j == 0:
                    sys_eq_matrix[i].append(1)
                else:
                    for indx in range(len(df_array[i])):
                        if indx != d_index:
                            sys_eq_matrix[i].append(df_array[i][indx])
                            break
        sys_matrix = Matrix(sys_eq_matrix)
        trans_sys_matrix = sys_matrix.transpose()
        new_sys_matrix = trans_sys_matrix @ sys_matrix
        inv_sys_matrix = new_sys_matrix.inverse()
        result = inv_sys_matrix @ trans_sys_matrix @ d_column
        return result
    
    def predict(self, input_dict):
        for val in self.coefficients.elements[0]:
            a = val
        for val in self.coefficients.elements[1]:
            b = val
        for key in input_dict:
            return a + b*input_dict[key]
