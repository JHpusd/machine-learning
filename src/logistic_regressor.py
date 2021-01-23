import sys
sys.path.append('src')
from dataframe import DataFrame
from matrix import Matrix
from linear_regressor import LinearRegressor
import math

class LogisticRegressor():
    def __init__(self, data, dependent_variable, upper_bound):
        self.df = data
        self.dv = dependent_variable
        self.up_bound = upper_bound
        self.coefficients = self.calc_coefficients()

    def calc_coefficients(self):
        df_transform = {key:self.df.data_dict[key] for key in self.df.data_dict}
        df_transform[self.dv] = [math.log((self.up_bound/i)-1) for i in df_transform[self.dv]]
        df_transform = DataFrame(df_transform, self.df.columns)
        linear_reg = LinearRegressor(df_transform, self.dv)
        return linear_reg.coefficients
    
    def predict(self, input_dict):
        coeff_sum = 0
        for key in self.coefficients:
            if key in input_dict:
                coeff_sum += self.coefficients[key] * input_dict[key]
            else:
                coeff_sum += self.coefficients[key]
        return self.up_bound/(1 + math.exp(coeff_sum))
