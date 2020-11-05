class Matrix():
    def __init__(self, input_elements):
        self.elements = input_elements
        self.num_rows = len(self.elements)
        self.num_cols = len(self.elements[0])

    def copy(self):
        clone_matrix = [[num for num in row] for row in self.elements]
        return Matrix(clone_matrix)

    def __add__(self, input_matrix):
        result = []
        for i in range(self.num_rows):
            result.append([])
            for j in range(self.num_cols):
                result[i].append(
                    self.elements[i][j] + input_matrix.elements[i][j])
        return Matrix(result)

    def __sub__(self, input_matrix):
        result = []
        for i in range(self.num_rows):
            result.append([])
            for j in range(self.num_cols):
                result[i].append(
                    self.elements[i][j] - input_matrix.elements[i][j])
        return Matrix(result)

    def __mul__(self, input_scalar):
        result = []
        for i in range(self.num_rows):
            result.append([])
            for j in range(self.num_cols):
                result[i].append(
                    round(self.elements[i][j] * input_scalar, 6))
        return Matrix(result)
    
    def __rmul__(self, input_scalar):
        result = []
        for i in range(self.num_rows):
            result.append([])
            for j in range(self.num_cols):
                result[i].append(
                    round(self.elements[i][j] * input_scalar, 6))
        return Matrix(result)

    def __matmul__(self, input_matrix):
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

    def __eq__(self, input_matrix):
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
            elif column_index > 0:
                if self.elements[i][column_index] != 0:
                    ref_num = 0
                    for j in self.elements[i][:column_index]:
                        ref_num += j
                    if ref_num == 0:
                        return i
                else:
                    continue
            else:
                return None

    def swap_rows(self, row_index_1, row_index_2):
        clone_matrix = self.copy()
        replacement = clone_matrix.elements[row_index_1]
        clone_matrix.elements[row_index_1] = clone_matrix.elements[row_index_2]
        clone_matrix.elements[row_index_2] = replacement
        return clone_matrix

    def normalize_row(self, row_index):
        clone_matrix = self.copy()
        for j in clone_matrix.elements[row_index]:
            if j != 0:
                initial_entry = j
                break
        for j in range(len(clone_matrix.elements[0])):
            clone_matrix.elements[row_index][j] /= initial_entry
        return clone_matrix

    def clear_below(self, row_index):
        clone_matrix = self.copy()
        for num in clone_matrix.elements[row_index]:
            if num != 0:
                j = num
                col_index = clone_matrix.elements[row_index].index(j)
                break
        for row in clone_matrix.elements[row_index + 1:]:
            if row[col_index] != 0:
                ref_num = row[col_index]
                for n in range(len(clone_matrix.elements[0])):
                    row[n] -= clone_matrix.elements[row_index][n]*ref_num
        return clone_matrix

    def clear_above(self, row_index):
        clone_matrix = self.copy()
        for num in clone_matrix.elements[row_index]:
            if num != 0:
                j = num
                col_index = clone_matrix.elements[row_index].index(j)
                break
        for row in clone_matrix.elements[:row_index]:
            if row[col_index] != 0:
                ref_num = row[col_index]
                for n in range(len(clone_matrix.elements[0])):
                    row[n] -= clone_matrix.elements[row_index][n]*ref_num
        return clone_matrix

    def rref(self):
        clone_matrix = self.copy()
        row_index = 0
        for j in range(clone_matrix.num_cols):
            pivot_index = clone_matrix.get_pivot_row(j)
            if pivot_index != None:
                if row_index not in range(clone_matrix.num_rows):
                    continue
                if pivot_index != row_index:
                    clone_matrix = clone_matrix.swap_rows(row_index, pivot_index)
                clone_matrix = clone_matrix.normalize_row(row_index)
                clone_matrix = clone_matrix.clear_above(row_index)
                clone_matrix = clone_matrix.clear_below(row_index)
                row_index += 1
            else:
                continue
        return clone_matrix

    def augment(self, other_matrix):
        clone_matrix = self.copy()
        assert clone_matrix.num_rows == other_matrix.num_rows
        for i in range(other_matrix.num_rows):
            for j in range(other_matrix.num_cols):
                clone_matrix.elements[i].append(other_matrix.elements[i][j])
        return clone_matrix
    
    def get_rows(self, row_nums):
        clone_matrix = self.copy()
        assert max(row_nums) <= clone_matrix.num_rows - 1
        result_matrix = []
        for row in row_nums:
            result_matrix.append(clone_matrix.elements[row])
        return Matrix(result_matrix)
    
    def get_columns(self, col_nums):
        clone_matrix = self.copy()
        assert max(col_nums) <= clone_matrix.num_cols - 1
        result_matrix = []
        for i in range(clone_matrix.num_rows):
            result_matrix.append([])
        for i in range(clone_matrix.num_rows):
            for column in col_nums:
                result_matrix[i].append(clone_matrix.elements[i][column])
        return Matrix(result_matrix)

    def inverse(self):
        clone_matrix = self.copy()
        if clone_matrix.num_rows != clone_matrix.num_cols:
            print("Error: cannot invert a non-square matrix")
            return
        identity_matrix = Matrix([[1 if j == i else 0 for j in range(clone_matrix.num_cols)] for i in range(clone_matrix.num_rows)])
        reduced_matrix = clone_matrix.augment(identity_matrix).rref()
        for i in range(clone_matrix.num_rows):
            if reduced_matrix.get_pivot_row(i) != i:
                print("Error: cannot invert a singular matrix")
                return
        result_matrix = []
        for i in range(clone_matrix.num_rows):
            result_matrix.append([])
            for j in range(clone_matrix.num_cols, reduced_matrix.num_cols):
                result_matrix[i].append(reduced_matrix.elements[i][j])
        return Matrix(result_matrix)
    
    def determinant(self):
        mult_constant = 1
        clone_matrix = self.copy()
        row_index = 0
        if clone_matrix.num_cols != clone_matrix.num_rows:
           return ("Error: Cannot take determinant of non-square matrix")
        for j in range(clone_matrix.num_cols):
            pivot_index = clone_matrix.get_pivot_row(j)
            if pivot_index != None:
                if row_index not in range(clone_matrix.num_rows):
                    continue
                if pivot_index != row_index:
                    clone_matrix = clone_matrix.swap_rows(row_index, pivot_index)
                    mult_constant *= -1
                mult_constant *= clone_matrix.elements[pivot_index][j]
                clone_matrix = clone_matrix.normalize_row(row_index)
                clone_matrix = clone_matrix.clear_above(row_index)
                clone_matrix = clone_matrix.clear_below(row_index)
                row_index += 1
            else:
                mult_constant *= 0
                continue
        return mult_constant
    
    def __pow__(self, power):
        identity_matrix = Matrix([[1 if j == i else 0 for j in range(self.num_cols)] for i in range(self.num_rows)])
        for _ in range(power):
            identity_matrix = identity_matrix @ (self)
        return identity_matrix

    def cofactor_num(self, row_num, col_num):
        cofactor_num = self.elements[row_num][col_num]
        sign = (row_num * self.num_cols) + col_num
        cofactor_num *= (-1)**sign
        return cofactor_num
    
    def cofactor_reducer(self, col_num):
        clone_matrix = self.copy()
        row_list = []
        for num in range(self.num_rows):
            if num != 0:
                row_list.append(num)
        col_list = []
        for num in range(self.num_cols):
            if num != col_num:
                col_list.append(num)
        new_matrix = clone_matrix.get_rows(row_list)
        new_matrix = new_matrix.get_columns(col_list)
        return new_matrix
    
    def cofactor_method_determinant(self):
        clone_matrix = self.copy()
        result = 0
        if clone_matrix.num_cols != clone_matrix.num_rows:
            return ("Error: Cannot take determinant of non-square matrix")
        if clone_matrix.num_cols == 2 and clone_matrix.num_rows == 2:
            first_cross = clone_matrix.elements[0][0] * clone_matrix.elements[1][1]
            second_cross = clone_matrix.elements[0][1] * clone_matrix.elements[1][0]
            return first_cross - second_cross
        else:
            for j in range(self.num_cols):
                mini_matrix = self.cofactor_reducer(j)
                reduced_matrix = mini_matrix.cofactor_method_determinant()
                result += self.cofactor_num(0, j) * reduced_matrix
            return result
