class GradientDescent():
    def __init__(self, function, init_point):
        self.func = function
        self.points = init_point
    
    def compute_gradient(self, delta):
        num_vars = self.func.__code__.co_argcount
        grad_list = []
        for i in range(num_vars):
            args_1 = list(self.points)
            args_2 = list(self.points)
            args_1[i] += 0.5*delta
            args_2[i] -= 0.5*delta
            derivative = ((self.func(*args_1) - self.func(*args_2))) / delta
            grad_list.append(derivative)
        return grad_list

    def descend(self, alpha, delta, num_steps):
        grad_list = self.compute_gradient(delta)
        for _ in range(num_steps):
            for i in range(len(grad_list)):
                self.points[i] -= alpha * grad_list[i]
        return
