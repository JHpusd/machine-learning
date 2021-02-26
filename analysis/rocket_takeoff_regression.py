import matplotlib.pyplot as plt
import sys
sys.path.append('src')
from polynomial_regressor import *

data = [(1, 3.1), (2, 10.17), (3, 20.93), (4, 38.71), (5, 60.91), (6, 98.87), (7, 113.92), (8, 146.95), (9, 190.09), (10, 232.65)]

df = DataFrame.from_array([[x[0],x[1]] for x in data], ['x', 'y'])
plt.style.use('bmh')
plt.plot([point[0] for point in data], [point[1] for point in data], 'ro', label='data')
poly_reg = PolynomialRegressor(2)
poly_reg.fit(df, 'y')
plt.plot([i for i in range(11)], [poly_reg.predict({'x': i}) for i in range(11)], label='quadratic')
'''
print(poly_reg.predict({'x': 5}))
print(poly_reg.predict({'x': 10}))
print(poly_reg.predict({'x': 200}))
'''

poly_reg = PolynomialRegressor(3)
poly_reg.fit(df, 'y')
plt.plot([i for i in range(11)], [poly_reg.predict({'x': i}) for i in range(11)], label='cubic')
'''
print(poly_reg.predict({'x': 5}))
print(poly_reg.predict({'x': 10}))
print(poly_reg.predict({'x': 200}))
'''
plt.xlabel('time')
plt.ylabel('position')
plt.legend(loc="upper left")
plt.savefig("rocket_model.png")

