
class SimplexAlg():
    def __init__(self, matrix_rep):
        self.matrix = matrix_rep # editing self.matrix will edit original matrix_rep
        self.expanded = False
        self.complete = False
    
    def constants(self):
        const = [row[len(row)-1] for row in self.matrix]
        const.pop()
        return const
    
    def gradients(self):
        grad = self.matrix[len(self.matrix)-1].copy()
        grad.pop()
        return grad
    
    def objective_val(self):
        last_row = self.matrix[len(self.matrix)-1]
        return -1 * last_row[len(last_row)-1]

    def get_col(self, i):
        return [row[i] for row in self.matrix]
    
    def insert_col(self, col_vals):
        assert len(col_vals) == len(self.matrix), 'insert_col, number of rows and new vals doesnt match'
        for i in range(len(col_vals)):
            row = self.matrix[i]
            val = col_vals[i]
            row.insert(len(row)-1, val)
    
    def make_expanded_matrix(self):
        num_constraints = len(self.matrix)-1
        bases = [[0 for row in self.matrix] for _ in range(num_constraints)]
        for i in range(len(bases)):
            base = bases[i]
            base[i] = 1
            self.insert_col(base)
        self.expanded = True
    
    def gradient_col(self):
        grad = self.gradients()
        return grad.index(max(grad))
    
    def constraint_row(self, col_index):
        col = self.get_col(col_index)
        col.pop()
        const = self.constants()
        constraints = [const[i]/col[i] for i in range(len(col))]
        const_copy = [i for i in constraints if i > 0]
        return constraints.index(min(const_copy))
    
    def elem_subtract(self, list_1, list_2): # pay attention to ordering
        assert len(list_1) == len(list_2), 'elem_subtract, lists are different lengths'
        return [round(list_1[i]-list_2[i], 6) for i in range(len(list_1))]
        # rounding to 6 decimal places here
    
    def const_mult(self, c, in_list):
        return [c*in_list[i] for i in range(len(in_list))]
    
    def clear_col(self, col_index, pivot_index): # pivot_index is row where pivot term is
        pivot_row = self.matrix[pivot_index]
        pivot_term = pivot_row[col_index]
        pivot_row = self.const_mult((1/pivot_term), pivot_row)
        self.matrix[pivot_index] = pivot_row
        assert pivot_row[col_index] == 1, 'clear col, calculation/code error in making pivot term 1'

        for i in range(len(self.matrix)):
            if i == pivot_index:
                continue
            row = self.matrix[i]
            col_term = row[col_index]
            self.matrix[i] = self.elem_subtract(row, self.const_mult(col_term, pivot_row))

    def iterate(self):
        if self.complete:
            print('attempted to run iteration while complete')
            return

        if not self.expanded:
            self.make_expanded_matrix()
        grad_col = self.gradient_col()
        const_row = self.constraint_row(grad_col)
        self.clear_col(grad_col, const_row)

        if all(grad <= 0 for grad in self.gradients()):
            self.complete = True
    
    def solve(self, print_iteration=False):
        iteration = 1
        while not self.complete:
            if print_iteration:
                print(f'iteration {iteration}')
            self.iterate()
            iteration += 1

