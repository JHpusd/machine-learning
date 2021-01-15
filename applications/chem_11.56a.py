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

data = {
    "x": [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,35],
    "y": [
        13.63,14.53,15.48,16.48,17.54,18.65,19.83,21.07,22.38,23.76,25.21,26.74,28.35,30.04,31.82,42.2]
}
data = DataFrame(data, ["x", "y"])
linear_reg = LinearRegressor(data, "y")
prediction = linear_reg.predict({
    "x": 37
})
print(prediction)
