import sys
sys.path.append('src')
from linear_regressor import *
from matrix import *
from dataframe import *
from logistic_regressor import *

class PolynomialRegressor():
    def __init__(self, degree):
        self.degree = degree
        self.dv = None
        self.df = None
        self.coefficients = None

    def fit(self, dataframe, dependent_var):
        self.dv = dependent_var
        new_dict = []
        new_cols = [col_name for col_name in dataframe.columns]
        if self.degree < 1:
            new_dict = [[pair[1]] for pair in dataframe.to_array()]
            new_cols.remove('x')
            self.df = DataFrame.from_array(new_dict, new_cols)
            self.coefficients = self.calculate_coefficients()
            return

        new_cols.remove(dependent_var)
        for i in range(len(dataframe.to_array())):
            new_dict.append([])
            for n in range(1, self.degree + 1):
                if n != 1 and "x^"+str(n) not in new_cols:
                    new_cols.append("x^" + str(n))
                new_dict[i].append(dataframe.to_array()[i][0]**n)
            new_dict[i].append(dataframe.to_array()[i][1])
        new_cols.append(dependent_var)
        self.df = DataFrame.from_array(new_dict, new_cols)
        self.coefficients = self.calculate_coefficients()
        return
    
    def calculate_coefficients(self):
        linear_reg = LinearRegressor(self.df, self.dv)
        return linear_reg.coefficients
    
    def predict(self, input_dict):
        all_cols = [col for col in self.df.columns]
        all_cols.remove(self.dv)
        
        for key in all_cols:
            if key not in input_dict and "^" in key:
                keys = key.split("^")
                input_dict[key] = input_dict[keys[0]] ** int(keys[1])

        result = 0
        for key in self.coefficients:
            if key in input_dict:
                result += self.coefficients[key] * input_dict[key]
            elif key not in input_dict:
                result += self.coefficients[key]
        return result
            



