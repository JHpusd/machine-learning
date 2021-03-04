import matplotlib.pyplot as plt
import math
import sys
sys.path.append('src')
from dataframe import *
from linear_regressor import *

data = [(0.0, 7.0),
 (0.2, 5.6),
 (0.4, 3.56),
 (0.6, 1.23),
 (0.8, -1.03),
 (1.0, -2.89),
 (1.2, -4.06),
 (1.4, -4.39),
 (1.6, -3.88),
 (1.8, -2.64),
 (2.0, -0.92),
 (2.2, 0.95),
 (2.4, 2.63),
 (2.6, 3.79),
 (2.8, 4.22),
 (3.0, 3.8),
 (3.2, 2.56),
 (3.4, 0.68),
 (3.6, -1.58),
 (3.8, -3.84),
 (4.0, -5.76),
 (4.2, -7.01),
 (4.4, -7.38),
 (4.6, -6.76),
 (4.8, -5.22)]

new_data = []
for x,y in data:
    new_data.append([math.sin(x), math.cos(x), math.sin(2*x), math.cos(2*x), y])
new_cols = ['sin(x)', 'cos(x)', 'sin(2x)', 'cos(2x)', 'y']

df = DataFrame.from_array(new_data, new_cols)
lin_reg = LinearRegressor(df, 'y')

plt.style.use('bmh')
plt.plot([x for x,y in data], [y for x,y in data], 'ro', label='data')
def signal_function(x):
    constant= lin_reg.coefficients['constant']
    sine_1 = lin_reg.coefficients['sin(x)']*math.sin(x)
    cosine_1 = lin_reg.coefficients['cos(x)']*math.cos(x)
    sine_2 = lin_reg.coefficients['sin(2x)']*math.sin(2*x)
    cosine_2 = lin_reg.coefficients['cos(2x)']*math.cos(2*x)
    return constant + sine_1 + cosine_1 + sine_2 + cosine_2
plt.plot([x for x,y in data], [signal_function(x) for x,y in data], label='model')

plt.legend(loc='upper right')
plt.savefig('signal_separation.png')

