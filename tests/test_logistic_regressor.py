import sys
sys.path.append('src')
from linear_regressor import *
from matrix import *
from dataframe import *
from logistic_regressor import *
'''
df = DataFrame.from_array(
    [[1,0.2],
     [2,0.25],
     [3,0.5]],
    columns = ['x','y']
)

log_reg = LogisticRegressor(df, 'y')
print(log_reg.predict({'x': 5}))

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
    [2, 2, 0.1],
    [3, 4, 0.1]],
    columns = ['beef', 'pb', 'rating'])
df = df.create_interaction_terms('beef', 'pb')

log_reg = LogisticRegressor(df, 'rating', 10)
# print(log_reg.coefficients)

print(log_reg.predict({
    'beef': 5,
    'pb': 0,
    'beef * pb': 0}))

print(log_reg.predict({
    'beef': 12,
    'pb': 0,
    'beef * pb': 0}))

print(log_reg.predict({
    'beef': 5,
    'pb': 5,
    'beef * pb': 25
}))
'''

df = DataFrame.from_array([[2,1], [3,0]], ['x', 'y'])
test = LogisticRegressor(df, 'y', 1)
test.set_coefficients({'constant': 1, 'x': 1})
test.gradient_descent(0.1, 0.1, 100, True)
