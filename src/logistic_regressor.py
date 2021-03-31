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
        try:
            self.coefficients = self.calc_coefficients()
        except:
            coeffs = list(self.df.columns)
            coeffs.remove(self.dv)
            coeffs.insert(0, 'constant')
            self.coefficients = {item:None for item in coeffs}

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
    
    def copy(self):
        return LogisticRegressor(self.df, self.dv, self.up_bound)

    def calc_rss(self):
        rss = 0
        df_arr = self.df.to_array()
        dv_index = self.df.columns.index(self.dv)
        no_dv_cols = list(self.df.columns)
        no_dv_cols.remove(self.dv)
        for row in df_arr:
            dv = row[dv_index]
            del row[dv_index]
            predict = {no_dv_cols[index]:row[index] for index in range(len(no_dv_cols))}
            prediction = self.predict(predict)
            rss += (prediction - dv) ** 2
        return rss
    
    def set_coefficients(self, new_coeffs):
        for key in self.coefficients:
            if key in new_coeffs:
                self.coefficients[key] = new_coeffs[key]
    
    def calc_gradient(self, delta):
        logreg_1 = self.copy()
        logreg_2 = self.copy()
        coeff_copy = dict(self.coefficients)
        gradients = {}
        for key in coeff_copy:
            coeffs_1 = dict(coeff_copy)
            coeffs_2 = dict(coeff_copy)
            coeffs_1[key] += 0.5 * delta
            coeffs_2[key] -= 0.5 * delta
            logreg_1.set_coefficients(coeffs_1)
            logreg_2.set_coefficients(coeffs_2)
            derivative = (logreg_1.calc_rss() - logreg_2.calc_rss()) / delta
            gradients[key] = derivative
        return gradients

    def gradient_descent(self, alpha, delta, num_steps, debug_mode=False):
        for i in range(num_steps):
            gradients = self.calc_gradient(delta)
            if debug_mode:
                print("Step {}:".format(i))
                print("\tGradient: "+str(gradients))
                print("\tCoeffs: "+str(self.coefficients))
                print("\tRSS: "+str(self.calc_rss())+"\n")
            for key in gradients:
                self.coefficients[key] -= gradients[key] * alpha

