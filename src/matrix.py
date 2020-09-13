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

    def get_pivot_row(self, column_index):
        for i in range(self.num_rows):
            if column_index == 0:
                if self.elements[i][column_index] != 0:
                    return i
            if column_index > 0:
                ref_num = 0
                for j in self.elements[i][:column_index]:
                    ref_num += j
                if ref_num == 0:
                    return i

    def swap_rows(self, row_index_1, row_index_2):
        replacement = self.elements[row_index_1]
        self.elements[row_index_1] = self.elements[row_index_2]
        self.elements[row_index_2] = replacement

    def normalize_row(self, row_index):
        for j in self.elements[row_index]:
            if j != 0:
                initial_entry = j
                break
        for j in range(self.num_cols):
            self.elements[row_index][j] /= initial_entry

    def clear_below(self, row_index):
        for num in self.elements[row_index]:
            if num != 0:
                j = num
                ref_index = self.elements[row_index].index(j)
                break
        for row in self.elements[row_index + 1:]:
            while row[ref_index] != 0:
                for n in range(self.num_cols):
                    row[n] -= self.elements[row_index][n]

    def clear_above(self, row_index):
        for num in self.elements[row_index]:
            if num != 0:
                j = num
                ref_index = self.elements[row_index].index(j)
                break
        for row in self.elements[:row_index]:
            while row[ref_index] != 0:
                for n in range(self.num_cols):
                    row[n] -= self.elements[row_index][n]
