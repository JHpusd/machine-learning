import sys
sys.path.append('src')
from linear_regressor import *
from matrix import *
from dataframe import *
'''
df = DataFrame.from_array([[1,0.2], [2,0.25], [3,0.5]], ['hours worked', 'progress'])

regressor = LinearRegressor(df, 'progress')

print("Testing that coefficients work...")
assert regressor.coefficients.round(6).elements == [[0.01667], [0.15]]
print("PASSED")
print("Testing method 'predict'...")
assert round(regressor.predict({'hours worked': 4}), 5) == 0.61667
print("PASSED")

print("Testing multi-variable linear regressor...")
df = DataFrame.from_array([[0, 0, 0.1],[1, 0, 0.2],[0, 2, 0.5],[4,5,0.6]], ['scoops of chocolate', 'scoops of vanilla', 'taste rating'])

regressor = LinearRegressor(df, 'taste rating')

coeff_dict = regressor.coefficients
for key in coeff_dict:
    coeff_dict[key] = round(coeff_dict[key], 8)
assert coeff_dict == {
    'constant': 0.19252336,
    'scoops of chocolate': -0.05981308,
    'scoops of vanilla': 0.13271028}

prediction = regressor.predict({
    'scoops of chocolate': 2,
    'scoops of vanilla': 3
    })
prediction = round(prediction, 8)
assert prediction == 0.47102804
print("PASSED")

df = DataFrame.from_array(
    [[0, 0, 1], 
    [1, 0, 2], 
    [2, 0, 4], 
    [4, 0, 8], 
    [6, 0, 9], 
    [0, 2, 2], 
    [0, 4, 5], 
    [0, 6, 7], 
    [0, 8, 6],
    [2, 2, 0],
    [3, 4, 0]],
    columns = ['beef', 'pb', 'rating']
)
df = df.create_interaction_terms('beef', 'pb')

regressor = LinearRegressor(df, 'rating')

print(regressor.predict({
    'beef': 5,
    'pb': 0,
    'beef * pb': 0
}))

print("data: " + str(regressor.df.data_dict))
print("columns: " + str(regressor.df.columns))

print(regressor.predict({
    'beef': 5,
    'pb': 5,
    'beef * pb': 25
}))
'''
