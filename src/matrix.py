class Matrix(input_elements):
    def __init__(self):
        self.elements = input_elements
    
    def copy(self):
        new_matrix = [[0, 0], [0, 0]]
        