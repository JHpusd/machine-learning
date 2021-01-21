import sys
sys.path.append('src')
from linear_regressor import *
from matrix import *
from dataframe import *
from logistic_regressor import *

df = DataFrame.from_array(
    [[1,0.2],
     [2,0.25],
     [3,0.5]],
    columns = ['x','y']
)

log_reg = LogisticRegressor(df, 'y')
print(log_reg.predict({'x': 5}))
