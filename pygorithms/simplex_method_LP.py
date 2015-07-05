from copy import deepcopy
import sys
import os
path = os.path.abspath("../pygorithms")
sys.path.append(path)
from simplex_LP_covnert_to_trivial_starting_verticie_form import\
    simplex_LP_covnert_to_trivial_starting_verticie_form\
        as convert_to_starting_form

sings = ("le", "eq", "ge")
simplex_table_statuses = ("Found optimal solution",
                          "No solution",
                          "Next Simplex table")
problem_types = ("min", "max")


class SimplexTable:

    def __init__(self, function_coefficients, Xb, Cb):
        self.function_coefficients = function_coefficients
        self.core_table = None
        self.Xb = Xb
        self.Cb = Cb
        self.B_slash = None
        self.C_slash = None


def simplex_method(function_coefficients, matrix_A,
                   vector_B, problem_type=problem_types[0],
                   signs_vector=None,
                   non_negative_constraints=None):
    """
    Solves a any linear optimization problem using Simplex LP
    The function takes 3 positional arguments and 3 keyword arguments

    function_coefficients which is a list that contains the coefficients
    of every variable of the problem
    matrix_A which is a list which contains list that consist of numbers
    every list in matrix_A represents a constraint and every constraint is
    a list of numbers that are the coefficients of the variables in each 
    constraint
    vector_B is a list that represents the RHS of each constraint 
    every number in the list corresponds to a constraint RHS
    problem_type is a keyword argument that takses a string
    which specifies the type of problem either a "min" or 
    "max" problem by default the value is "min"
    signs_vector is a list that consists of strings which 
    represent each constraint signs possible options are
    greater than or equal which is the string "ge"
    less that or equal which is the string "le"
    or equal which is the string "eq"
    by default tha list consists of "eq" string this means
    that all constraint are equations
    non_negative_constraints is a list that consists of booleans
    each boolean corresponds to a variable if it is True
    then there is a non negativity constraint for the variable
    by default all avariables are non negative thus the list 
    is filled with values True

    Example usage:
    The mathematical problem:
    min Z = -5*x1 + 2*x2
    subject to the constraints
    1*x1 -1*x2 >= 2
    1*x1 -2*x2 >= 0
    2*x1 -1*x2 <= 1
    x1>=0

    This porblem transforms to :
        function_coefficients = [-5, 2]
        matrix_A = [[1, -1],
                    [1, -2],
                    [2, -1]]
        vector_B = [2, 0, 1]
        problem_type = "min"
        signs_vector = ["ge", "ge", "le"]
        non_negative_constraints = [True, False]

    when you call the function simplex_method
    with the arguments in the order in the example
    you will get a return value that is a tuple of two
    elements the first one is the optimal value
    and the second is a list that represents the coefficients
    of the variables in the optimal solution
    in case there is no optimal or feasible solution
    an exception will be raised.
    If there is an invalid input you will get and exception
    depending on the input error that you have mede.
    """
    if signs_vector is None:
        signs_vector = [sings[1] for _ in range(len(vector_B))]
    if non_negative_constraints is None:
        non_negative_constraints = [True for _ in range(
            len(function_coefficients))]
    function_coefficients, matrix_A, vector_B = convert_to_starting_form(
        function_coefficients, matrix_A, vector_B, problem_type,
        signs_vector, non_negative_constraints)
    Xb = _calculate_Xb(matrix_A)
    Cb = _calculate_Cb(function_coefficients, Xb)
    first_simplex_table = SimplexTable(function_coefficients, Xb, Cb)
    first_simplex_table.core_table = matrix_A  # DEEP copy minght not be needed
    first_simplex_table.B_slash = vector_B
    first_simplex_table.C_slash = _calculate_C_slash(first_simplex_table)
    simplex_table = first_simplex_table
    while True:
        simplex_table_status = _check_simplex_table_optimality(simplex_table)

        if simplex_table_status == simplex_table_statuses[0]:
            return _get_optimal_solution(
                simplex_table, problem_type, non_negative_constraints,
                signs_vector)
        elif simplex_table_status == simplex_table_statuses[1]:
            raise NoOptimalSolutionError

        simplex_table = _new_simplex_table(simplex_table)


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


def _get_optimal_solution(
    simplex_table, problem_type, non_negative_constraints,
        signs_vector):

    optimal_vertex = _calculate_optimal_vertex(
        simplex_table, non_negative_constraints, signs_vector)
    if problem_type == problem_types[0]:
        optimal_value = -simplex_table.C_slash[-1]
    elif problem_type == problem_types[1]:
        optimal_value = simplex_table.C_slash[-1]

    return optimal_value, optimal_vertex


def _calculate_optimal_vertex(
        simplex_table, non_negative_constraints, signs_vector):

    initial_variables_count = len(non_negative_constraints)
    additional_negative_vars_count = sum(
        [1 for i in non_negative_constraints if i is False])
    additional_not_eq_signs_equations_count = sum(
        [1 for i in signs_vector if i != sings[1]])

    additional_artificial_variables_count =\
        len(simplex_table.function_coefficients) - (
            initial_variables_count + additional_negative_vars_count +
            additional_not_eq_signs_equations_count)

    optimal_vertex = []
    for variable in range(len(simplex_table.function_coefficients)):

        if variable in simplex_table.Xb:
            index = simplex_table.Xb.index(variable)
            optimal_vertex.append(simplex_table.B_slash[index])
        else:
            optimal_vertex.append(0)

    if additional_artificial_variables_count > 0:
        artificial_variables_values = optimal_vertex[
            -additional_artificial_variables_count:]
    else:
        artificial_variables_values = []

    non_zero_artificial_variables_values = [
        i for i in artificial_variables_values if i > 0]

    if non_zero_artificial_variables_values != []:
        raise NoFeasibleSolutionError

    # if additional_artificial_variables_count > 0:
    #     optimal_vertex = optimal_vertex[:-additional_artificial_variables_count]

    optimal_vertex = optimal_vertex[:-additional_artificial_variables_count]\
        or optimal_vertex

    for index, variable in enumerate(iter(non_negative_constraints)):
        if variable is False:
            optimal_vertex[index] = optimal_vertex[
                index] - optimal_vertex[index+1]
            optimal_vertex.pop(index + 1)
    optimal_vertex = optimal_vertex[
        :-additional_not_eq_signs_equations_count] or optimal_vertex
    return optimal_vertex


def _check_simplex_table_optimality(simplex_table):
    no_optimal_solution = False
    C_slash_duplicate = []
    for j, value in enumerate(iter(simplex_table.C_slash[:-1])):
        if value < 0:
            for i in range(len(simplex_table.Xb)):
                if simplex_table.core_table[i][j] > 0:
                    break
                if i == len(simplex_table.Xb) - 1:
                    no_optimal_solution = True
            continue
        C_slash_duplicate.append(value)

    if no_optimal_solution:
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
    for i in range(len(simplex_table.Xb)):
        j = lowest_value_index
        if simplex_table.core_table[i][j] > 0:
            key_elemenent_candidates.append([simplex_table.core_table[i][j], i])

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
    key_element, out_in_basis, key_coords = _find_key_element(simplex_table)

    new_Xb = _new_simplex_table_Xb(simplex_table.Xb, out_in_basis)
    new_Cb = _calculate_Cb(simplex_table.function_coefficients, new_Xb)
    new_simplex_table = SimplexTable(
        simplex_table.function_coefficients, new_Xb, new_Cb)
    new_core_table = deepcopy(simplex_table.core_table)
    new_B_slash = deepcopy(simplex_table.B_slash)

    key_i = key_coords[0]
    key_j = key_coords[1]

    for k in range(len(simplex_table.B_slash)):
        for v in range(len(simplex_table.function_coefficients)):
            if k == key_i:
                new_core_table[k][v] = simplex_table.core_table[k][v]/key_element
            else:
                new_core_table[k][v] = simplex_table.core_table[k][v] - (simplex_table.core_table[key_i][v]*simplex_table.core_table[k][key_j])/key_element

    for k in range(len(simplex_table.B_slash)):
        if k == key_i:
            new_B_slash[k] = simplex_table.B_slash[k]/key_element
        else:
            new_B_slash[k] = simplex_table.B_slash[k] - simplex_table.B_slash[key_i]*simplex_table.core_table[k][key_j]/key_element

    new_simplex_table.core_table = new_core_table
    new_simplex_table.B_slash = new_B_slash
    new_simplex_table.C_slash = _calculate_C_slash(new_simplex_table)
    return new_simplex_table



class NoOptimalSolutionError(Exception):
    pass

class NoFeasibleSolutionError(Exception):
    pass