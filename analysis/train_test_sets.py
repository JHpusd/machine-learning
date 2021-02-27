import matplotlib.pyplot as plt
import sys
sys.path.append('src')
from linear_regressor import *
from polynomial_regressor import *
from dataframe import *

data = [(-4, 11.0),
 (-2, 5.0),
 (0, 3.0),
 (2, 5.0),
 (4, 11.1),
 (6, 21.1),
 (8, 35.1),
 (10, 52.8),
 (12, 74.8),
 (14, 101.2)]

training_set = [[p[0], p[1]] for p in data if data.index(p)%2 == 0]
test_set = [[p[0], p[1]] for p in data if data.index(p)%2 == 1]

train_df = DataFrame.from_array(training_set, ['x', 'y'])
test_df = DataFrame.from_array(test_set, ['x', 'y'])

lin_reg = LinearRegressor(train_df, 'y')
'''
print("linear regressor: ")
rss = 0
for coord in training_set:
    rss += (coord[1] - lin_reg.predict({'x': coord[0]}))**2
print("training set rss: " + str(rss))
rss = 0
for coord in test_set:
    rss += (coord[1] - lin_reg.predict({'x': coord[0]}))**2
print("test set rss: " + str(rss) + "\n")
'''
quad_reg = PolynomialRegressor(2)
quad_reg.fit(train_df, 'y')
'''
print("quadratic regressor: ")
rss = 0
for coord in training_set:
    rss += (coord[1] - quad_reg.predict({'x': coord[0]}))**2
print("training set rss: " + str(rss))
rss = 0
for coord in test_set:
    rss += (coord[1] - quad_reg.predict({'x': coord[0]}))**2
print("test set rss: " + str(rss) + "\n")
'''
cube_reg = PolynomialRegressor(3)
cube_reg.fit(train_df, 'y')
'''
print("cubic regressor: ")
rss = 0
for coord in training_set:
    rss += (coord[1] - cube_reg.predict({'x': coord[0]}))**2
print("training set rss: " + str(rss))
rss = 0
for coord in test_set:
    rss += (coord[1] - cube_reg.predict({'x': coord[0]}))**2
print("test set rss: " + str(rss) + "\n")
'''
quart_reg = PolynomialRegressor(4)
quart_reg.fit(train_df, 'y')
'''
print("quartic regressor: ")
rss = 0
for coord in training_set:
    rss += (coord[1] - quart_reg.predict({'x': coord[0]}))**2
print("training set rss: " + str(rss))
rss = 0
for coord in test_set:
    rss += (coord[1] - quart_reg.predict({'x': coord[0]}))**2
print("test set rss: " + str(rss) + "\n")
'''
plt.style.use('bmh')
plt.plot([point[0] for point in data], [point[1] for point in data], 'ro', label='data')
plt.plot([i for i in range(-15,16)], [lin_reg.predict({'x':i}) for i in range(-15,16)], label='linear')
plt.plot([i for i in range(-15,16)], [quad_reg.predict({'x':i}) for i in range(-15,16)], label='quadratic')
plt.plot([i for i in range(-15,16)], [cube_reg.predict({'x':i}) for i in range(-15,16)], label='cubic')
plt.plot([i for i in range(-15,16)], [quart_reg.predict({'x':i}) for i in range(-15,16)], label='quartic')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='lower right', prop={'size': 8})
plt.savefig('train_test_set_models.png')
