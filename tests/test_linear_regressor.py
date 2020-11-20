import sys
sys.path.append('src')
from linear_regressor import *
from matrix import *
from dataframe import *

df = DataFrame.from_array([[1,0.2], [2,0.25], [3,0.5]], ['hours worked', 'progress'])

regressor = LinearRegressor(df, 'progress')

print("Testing that coefficients work...")
assert regressor.coefficients.round(6).elements == [[0.01667], [0.15]]
print("PASSED")
print("Testing method 'predict'...")
assert round(regressor.predict({'hours worked': 4}), 5) == 0.61667
print("PASSED")
