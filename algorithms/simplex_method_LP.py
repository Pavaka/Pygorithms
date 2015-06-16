from copy import deepcopy
sings = ("le", "eq", "ge")
simplex_table_statuses = ("Found optimal solution", "No feasible solution")

class SimplexTable:

    def __init__(self, function_coefficients, Xb, Cb):
        self.function_coefficients = function_coefficients
        self.core_table = None
        self.Xb = Xb
        self.Cb = Cb
        self.B_slash = None
        self.C_slash = None


def simplex_method(problem_type, function_coefficients,
                   matrix_A, signs_vector, vector_B, non_negative_constraints):
    pass

    # CHECK INPUT DATA
    # POSSIBLE CONVRSION OT CANONICAL format

    Xb = _find_starting_vertex(matrix_A)
    Cb = _calculate_Cb(Xb)
    first_simplex_table = SimplexTable(function_coefficients, Xb, Cb)
    first_simplex_table.core_table = matrix_A  # DEEP copy minght not be needed
    first_simplex_table.B_slash = vector_B
    first_simplex_table.C_slash = _calculate_C_slash(first_simplex_table)
    simplex_table = first_simplex_table

    while True:
        simplex_table_status = _check_simplex_table_optimality(simplex_table)
        if simplex_table_status == simplex_table_statuses[0]:
            return #the optimal solution
        elif simplex_table_status == simplex_table_statuses[1]:
            raise # No feasible solution error


def _find_starting_vertex(matrix_A):
    matrix_rows = len(matrix_A)
    matrix_columns = len(matrix_A[0])
    starting_vertex = []
    add_item_flag = False
    for i in range(matrix_rows):
        for j in range(matrix_columns):

            if matrix_A[i][j] > 0:
                for index in range(0, matrix_rows):
                    if index == i:
                        continue
                    if matrix_A[index][j] != 0:
                        add_item_flag = False
                        break
                    add_item_flag = True
                if add_item_flag and len(starting_vertex) < matrix_rows:
                    starting_vertex.append(j)
    return sorted(starting_vertex)


def _calculate_Cb(Xb):
    Cb = []
    return list(map(Cb.append, Xb))


def _calculate_C_slash(simplex_table):
    ST = simplex_table
    C_slash_len = len(ST.function_coefficients)
    Cb_len = len(ST.Cb)
    C_slash = []
    for j in range(C_slash_len):
        C_slash.append(ST.function_coefficients[j])
        for i in range(Cb_len):
            C_slash[j] -= ST.Cb[i] * ST.core_table[i][j]

    function_value = -sum(map(lambda x, y: x*y, ST.Cb, ST.B_slash))
    C_slash.append(function_value)

    return C_slash
