class Matrix():
    def __init__(self, input_elements):
        self.elements = input_elements
        self.num_rows = len(self.elements)
        self.num_cols = len(self.elements[0])

    def copy(self):
        return self

    def add(self, input_matrix):
        result = []
        for i in range(self.num_rows):
            result.append([])
            for j in range(self.num_cols):
                result[i].append(
                    self.elements[i][j] + input_matrix.elements[i][j])
        return Matrix(result)

    def subtract(self, input_matrix):
        result = []
        for i in range(self.num_rows):
            result.append([])
            for j in range(self.num_cols):
                result[i].append(
                    self.elements[i][j] - input_matrix.elements[i][j])
        return Matrix(result)

    def scalar_multiply(self, input_scalar):
        result = []
        for i in range(self.num_rows):
            result.append([])
            for j in range(self.num_cols):
                result[i].append(
                    self.elements[i][j] * input_scalar)
        return Matrix(result)

    def matrix_multiply(self, input_matrix):
        result = []
        for i in range(self.num_rows):
            result.append([])
            for j in range(input_matrix.num_cols):
                result[i].append(0)
        for i in range(self.num_rows):
            for j in range(input_matrix.num_cols):
                for k in range(input_matrix.num_rows):
                    result[i][j] += (
                        self.elements[i][k] * input_matrix.elements[k][j])
        return Matrix(result)

    def transpose(self):
        result = []
        for i in range(self.num_cols):
            result.append([])
            for j in range(self.num_rows):
                result[i].append(self.elements[j][i])
        return Matrix(result)

    def is_equal(self, input_matrix):
        if self.elements == input_matrix.elements:
            return True
        else:
            return False
    
    def round(self, decimal_places):
        for i in self.elements:
            for j in range(len(i)):
                i[j] = round(i[j], 5)
        return Matrix(self.elements)