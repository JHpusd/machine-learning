class Matrix():
    def __init__(self, input_elements):
        self.elements = input_elements

    def copy(self):
        new_matrix = Matrix(self.elements)
        return new_matrix

    def add(self, input_matrix):
        result = [[0, 0], [0, 0]]
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                result[i][j] = (
                    self.elements[i][j] + input_matrix.elements[i][j])
        return Matrix(result)

    def subtract(self, input_matrix):
        result = [[0, 0], [0, 0]]
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                result[i][j] = (
                    self.elements[i][j] - input_matrix.elements[i][j])
        return Matrix(result)

    def scalar_multiply(self, input_scalar):
        result = [[0, 0], [0, 0]]
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                result[i][j] = self.elements[i][j] * input_scalar
        return Matrix(result)

    def matrix_multiply(self, input_matrix):
        result = [[0, 0], [0, 0]]
        for i in range(len(self.elements)):
            for j in range(len(input_matrix.elements[0])):
                for k in range(len(input_matrix.elements)):
                    result[i][j] += (
                        self.elements[i][k] * input_matrix.elements[k][j])
        return Matrix(result)
