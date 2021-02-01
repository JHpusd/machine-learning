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
        all_cols = [col for col in self.df.columns]
        all_cols.remove(self.dv)
        
        for key in all_cols:
            if key not in input_dict and " * " not in key:
                input_dict[key] = 0
            if key not in input_dict and " * " in key:
                keys = key.split(" * ")
                input_dict[key] = input_dict[keys[0]] * input_dict[keys[1]]

        coeff_sum = 0
        for key in self.coefficients:
            if key in input_dict:
                coeff_sum += self.coefficients[key] * input_dict[key]
            else:
                coeff_sum += self.coefficients[key]
        return self.up_bound/(1 + math.exp(coeff_sum))
