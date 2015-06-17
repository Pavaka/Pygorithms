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

        simplex_table = new_simplex_table(simplex_table)


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


def _find_key_element(simplex_table):
    lowest_value = min(simplex_table.C_slash[:-1])
    lowest_value_index = simplex_table.C_slash.index(lowest_value)
    coefficient_column = []

    for row in simplex_table.core_table:
        coefficient_column.append(
            row[lowest_value_index])

    key_elemenent_candidates = []
    for j in range(len(simplex_table.Xb)):
        i = lowest_value_index
        if simplex_table.core_table[i][j] > 0:
            key_elemenent_candidates.append([simplex_table.core_table[i][j], j])

    for element in key_elemenent_candidates:
        element[0] = simplex_table.B_slash[element[1]] / element[0]

    key_element_index = min(key_elemenent_candidates, key = lambda x: x[0])[1]
    key_element = simplex_table.core_table[lowest_value_index][key_element_index]
    out_of_basis_X = simplex_table.Xb[key_element_index]
    going_in_basis_X = lowest_value_index

    return key_element, [out_of_basis_X, going_in_basis_X], (key_element_index, lowest_value_index)

def _new_simplex_table_Xb(Xb, basis_rotation):
    index = Xb.index(basis_rotation[0])
    Xb[index] = basis_rotation[1]
    return Xb


def _new_simplex_table(simplex_table):
    key_element = _find_key_element(simplex_table)
    new_Xb = _new_simplex_table_Xb(simplex_table.Xb, key_element[1])
    new_Cb = _calculate_Cb(simplex_table.function_coefficients, new_Xb)
    new_simplex_table = SimplexTable(
        simplex_table.function_coefficients, new_Xb, new_Cb)
    new_core_table = deepcopy(simplex_table.core_table)
    new_B_slash = deepcopy(simplex_table.B_slash)

    key_i = key_element[2][0]
    key_j = key_element[2][1]
    # new key row
    for j in range(len(simplex_table.function_coefficients)):
        new_core_table[key_i][j] = simplex_table.core_table[key_i][j]/key_element[0]

    new_B_slash[key_i] = simplex_table.B_slash[key_i]/key_element[0]
    print(simplex_table.core_table)
    print(key_i, key_j)
    for k in range(len(simplex_table.B_slash)):
        if k == key_i:
            continue
        for v in range(len(simplex_table.C_slash) - 1):
            if v == len(simplex_table.C_slash) - 1:

                try:
                    # print("cacl b slash")
                    new_B_slash[k] = key_element[0] - simplex_table.B_slash[key_i]*simplex_table.core_table[k][key_j]/simplex_table.B_slash[k]
                    # print(k,v, "new_b slash", new_B_slash[k])

                except ZeroDivisionError:
                    new_B_slash[k] = 0 
                continue

            try:
                new_core_table[k][v] = key_element[0] - simplex_table.core_table[key_i][v]*simplex_table.core_table[k][key_j]/simplex_table.core_table[k][v]
                print("new core table", k, v, new_core_table[k][v], key_element[0], simplex_table.core_table[key_i][v], simplex_table.core_table[k][key_j], simplex_table.core_table[k][v])
            except ZeroDivisionError:
                new_core_table[k][v] = 0
                print("new core table zero ZeroDivisionError")


    print(new_core_table, new_B_slash)




class NoFeasibleSolutionError(Exception):
    pass