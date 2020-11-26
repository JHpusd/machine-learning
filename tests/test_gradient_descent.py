import sys
sys.path.append('src')
from gradient_descent import GradientDescent

def single_variable_function(x):
    return (x-1)**2
def two_variable_function(x, y):
    return (x-1)**2 + (y-1)**3
def three_variable_function(x, y, z):
    return (x-1)**2 + (y-1)**3 + (z-1)**4
def six_variable_function(x1, x2, x3, x4, x5, x6):
    return (x1-1)**2 + (x2-1)**3 + (x3-1)**4 + x4 + 2*x5 + 3*x6

print("Testing gradient descent methods on mult-variable function...")

minimizer = GradientDescent(single_variable_function, [0])
assert minimizer.points == [0]
grad_list = minimizer.compute_gradient(0.01)
for i in range(len(grad_list)):
    grad_list[i] = round(grad_list[i], 5)
assert grad_list == [-2.00000]
minimizer.descend(0.001, 0.01, 1)
for i in range(len(minimizer.points)):
    minimizer.points[i] = round(minimizer.points[i], 5)
assert minimizer.points == [0.00200]

minimizer = GradientDescent(two_variable_function, [0 ,0])
assert minimizer.points == [0, 0]
grad_list = minimizer.compute_gradient(0.01)
for i in range(len(grad_list)):
    grad_list[i] = round(grad_list[i], 5)
assert grad_list == [-2.00000, 3.00002]
minimizer.descend(0.001, 0.01, 1)
for i in range(len(minimizer.points)):
    minimizer.points[i] = round(minimizer.points[i], 5)
assert minimizer.points == [0.00200, -0.00300]

minimizer = GradientDescent(three_variable_function, [0 ,0, 0])
assert minimizer.points == [0, 0, 0]
grad_list = minimizer.compute_gradient(0.01)
for i in range(len(grad_list)):
    grad_list[i] = round(grad_list[i], 5)
assert grad_list == [-2.00000, 3.00002, -4.00010]
minimizer.descend(0.001, 0.01, 1)
for i in range(len(minimizer.points)):
    minimizer.points[i] = round(minimizer.points[i], 5)
assert minimizer.points == [0.00200, -0.00300, 0.00400]

minimizer = GradientDescent(six_variable_function, [0,0,0,0,0,0])
assert minimizer.points == [0,0,0,0,0,0]
grad_list = minimizer.compute_gradient(0.01)
for i in range(len(grad_list)):
    grad_list[i] = round(grad_list[i], 5)
assert grad_list == [-2.00000, 3.00002, -4.00010, 1.00000, 2.00000, 3.00000]
minimizer.descend(0.001, 0.01, 1)
for i in range(len(minimizer.points)):
    minimizer.points[i] = round(minimizer.points[i], 5)
assert minimizer.points == [0.00200, -0.00300, 0.00400, -0.00100, -0.00200, -0.00300]
print("PASSED")
