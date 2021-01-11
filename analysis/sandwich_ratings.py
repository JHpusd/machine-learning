import sys
sys.path.append('src')
from linear_regressor import *
from matrix import *
from dataframe import *

df = DataFrame.from_array([[0,0,1], [1,0,2], [2,0,4], [4,0,8], [6,0,9], [0,2,2], [0,4,5], [0,6,7], [0,8,6]], ['slices of roast beef', 'tablespoons of peanut butter', 'rating'])

regressor = LinearRegressor(df, 'rating')

prediction_1 = regressor.predict({
    'slices of roast beef': 5,
    'tablespoons of peanut butter': 0
})
print('5 slices of roast beef, 0 tablespoons of pb: ' + str(prediction_1))

prediction_2 = regressor.predict({
    'slices of roast beef': 5,
    'tablespoons of peanut butter': 5
})
print('5 slices of roast beef, 5 tablespoons of pb: ' + str(prediction_2))
