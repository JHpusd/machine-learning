import sys
sys.path.append('src')
from polynomial_regressor import *

df = DataFrame.from_array(
    [(0,1), (1,2), (2,5), (3,10), (4,20), (5,30)],
    columns = ['x', 'y'])

print("constant regressor: ")
constant_regressor = PolynomialRegressor(0)
constant_regressor.fit(df, 'y')
print("coefficients: " + str(constant_regressor.coefficients))
print("prediction: " + str(constant_regressor.predict({'x': 2})) + '\n')

print("linear_regressor: ")
linear_regressor = PolynomialRegressor(1)
linear_regressor.fit(df, 'y')
print("coefficients: " + str(linear_regressor.coefficients))
print("prediction: " + str(linear_regressor.predict({'x': 2})) + "\n")

print("quadratic_regressor: ")
quadratic_regressor = PolynomialRegressor(2)
quadratic_regressor.fit(df, 'y')
print("coefficients: " + str(quadratic_regressor.coefficients))
print("prediction: " + str(quadratic_regressor.predict({'x': 2})) + "\n")

print("cubic_regressor: ")
cubic_regressor = PolynomialRegressor(3)
cubic_regressor.fit(df, 'y')
print("coefficients: " + str(cubic_regressor.coefficients))
print("prediction: " + str(cubic_regressor.predict({'x': 2})) + "\n")

print("quintic_regressor: ")
quintic_regressor = PolynomialRegressor(5)
quintic_regressor.fit(df, 'y')
print("coefficients: " + str(quintic_regressor.coefficients))
print("prediction: " + str(quintic_regressor.predict({'x': 2})))


