from copy import deepcopy
sings = ("le", "eq", "ge")
simplex_table_statuses = ("Found optimal solution",
                          "No feasible solution", "Next Simplex table")
problem_types = ("min", "max")


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

    Xb = _calculate_Xb(matrix_A)
    Cb = _calculate_Cb(Xb)
    first_simplex_table = SimplexTable(function_coefficients, Xb, Cb)
    first_simplex_table.core_table = matrix_A  # DEEP copy minght not be needed
    first_simplex_table.B_slash = vector_B
    first_simplex_table.C_slash = _calculate_C_slash(first_simplex_table)
    simplex_table = first_simplex_table

    while True:
        simplex_table_status = _check_simplex_table_optimality(simplex_table)

        if simplex_table_status == simplex_table_statuses[0]:
            return _get_optimal_solution(problem_type, simplex_table)
        elif simplex_table_status == simplex_table_statuses[1]:
            raise NoFeasibleSolutionError


def _calculate_Xb(matrix_A):
    matrix_rows = len(matrix_A)
    matrix_columns = len(matrix_A[0])
    Xb = []
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
                if add_item_flag and len(Xb) < matrix_rows:
                    Xb.append(j)
    return Xb


def _calculate_Cb(function_coefficients, Xb):
    Cb = []
    for x in Xb:
        Cb.append(function_coefficients[x])
    return Cb


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


def _get_optimal_solution(simplex_table, problem_type="min"):
    if problem_type == problem_types[0]:
        optimal_value = -simplex_table.C_slash[-1]
    elif problem_type == problem_types[1]:
        optimal_value = -simplex_table.C_slash[-1]

    optimal_vertex = []

    for variable in range(len(simplex_table.function_coefficients)):

        if variable in simplex_table.Xb:
            index = simplex_table.Xb.index(variable)
            optimal_vertex.append(simplex_table.B_slash[index])
        else:
            optimal_vertex.append(0)

    return optimal_value, optimal_vertex


def _check_simplex_table_optimality(simplex_table):
    no_feasible_solution = False
    C_slash_duplicate = []
    for i, value in enumerate(simplex_table.C_slash[:-1]):
        if value < 0:
            for j in range(len(simplex_table.Xb)):
                if simplex_table.core_table[i][j] >= 0:
                    break
                if j == len(simplex_table.Xb) - 1:
                    no_feasible_solution = True
            continue
        C_slash_duplicate.append(value)

    if no_feasible_solution:
        return simplex_table_statuses[1]
    elif len(C_slash_duplicate) == len(simplex_table.C_slash[:-1]):
        return simplex_table_statuses[0]
    else:
        return simplex_table_statuses[2]



class NoFeasibleSolutionError(Exception):
    pass
