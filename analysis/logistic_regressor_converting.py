import matplotlib.pyplot as plt
import sys
sys.path.append('src')
from dataframe import *
from logistic_regressor import *

df = DataFrame.from_array(
    [[1,0],
    [2,0],
    [3,0],
    [2,1],
    [3,1],
    [4,1]],
    ['x', 'y'])
plt.style.use('bmh')
plt.plot([row[0] for row in df.to_array()], [row[1] for row in df.to_array()],'ro')

def log_reg_convert_zeros_and_ones(dataframe, dv, delta):
    dv_index = dataframe.columns.index(dv)
    new_array = []
    for row in dataframe.to_array():
        if row[dv_index] == 0:
            row[dv_index] += delta
        elif row[dv_index] == 1:
            row[dv_index] -= delta
        new_array.append(row)
    return DataFrame.from_array(new_array, dataframe.columns)

df1 = log_reg_convert_zeros_and_ones(df, 'y', 0.1)
logreg1 = LogisticRegressor(df1, 'y', 1)
plt.plot([i*0.01 for i in range(401)], [logreg1.predict({'x':i*0.01}) for i in range(401)], label='0.1')

df2 = log_reg_convert_zeros_and_ones(df, 'y', 0.01)
logreg2 = LogisticRegressor(df2, 'y', 1)
plt.plot([i*0.01 for i in range(401)], [logreg2.predict({'x':i*0.01}) for i in range(401)],label='0.01')

df3 = log_reg_convert_zeros_and_ones(df, 'y', 0.001)
logreg3 = LogisticRegressor(df3, 'y', 1)
plt.plot([i*0.01 for i in range(401)], [logreg3.predict({'x':i*0.01}) for i in range(401)],label='0.001')

df4 = log_reg_convert_zeros_and_ones(df, 'y', 0.0001)
logreg4 = LogisticRegressor(df4, 'y', 1)
plt.plot([i*0.01 for i in range(401)], [logreg4.predict({'x':i*0.01}) for i in range(401)],label='0.0001')
plt.legend(loc='upper left')
plt.savefig('logistic_regressor_conversion.png')
