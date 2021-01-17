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
                if j != d_index:
                    sys_eq_matrix[i].append(df_array[i][j])
                elif j == d_index:
                    continue
        sys_matrix = Matrix(sys_eq_matrix)
        trans_sys_matrix = sys_matrix.transpose()
        new_sys_matrix = trans_sys_matrix @ sys_matrix
        inv_sys_matrix = new_sys_matrix.inverse()
        coeff_matrix = inv_sys_matrix @ trans_sys_matrix @ d_column
        coeff_dict = {}
        self.df.columns.remove(self.dv)
        for i in range(len(self.df.columns) + 1):
            if i == 0:
                coeff_dict['constant'] = coeff_matrix.elements[i][0]
            elif i != 0:
                coeff_dict[self.df.columns[i-1]] = coeff_matrix.elements[i][0]
        return coeff_dict
    
    def predict(self, input_dict):
        result = 0
        for key in self.coefficients:
            if key in input_dict:
                result += self.coefficients[key] * input_dict[key]
            elif key not in input_dict:
                result += self.coefficients[key]
            
        return result

