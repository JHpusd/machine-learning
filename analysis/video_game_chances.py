import sys
sys.path.append('src')
from logistic_regressor import *
from matrix import *
from dataframe import *

data = [(10, 0.05), (100, 0.35), (1000, 0.95)]
data = [[point[0], point[1]] for point in data]
df = DataFrame.from_array(data, ['hours', 'chances'])

log_reg = LogisticRegressor(df, 'chances', 1)

# print(log_reg.predict({'hours': 500}))

beta_0 = log_reg.coefficients['constant']
beta_1 = log_reg.coefficients['hours']

# print((math.log(1/math.exp(beta_0))) / beta_1)
# equation was worked out on paper

