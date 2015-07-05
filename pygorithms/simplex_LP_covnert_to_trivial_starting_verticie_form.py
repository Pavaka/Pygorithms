import sys
import os
sys.path.append(os.path.abspath(".."))
from input_checkers.SM_input_checker import check_input_data

signs = ("le", "eq", "ge")
problem_types = ("min", "max")
big_M = 2 ** 20


def simplex_LP_covnert_to_trivial_starting_verticie_form(
    function_coefficients, matrix_A,
        vector_B, problem_type, signs_vector,
        non_negative_constraints):
    """
    Function that takes the same type and number of arguments
    like simlex_method_LP (for more info check help(simlex_method_LP))
    The function returns a modified function_coefficients, matrix_A and
    vector_B so that they are in form with trivial verticie so the simlpex
    method can make a simlpex table and start iterating.
    """

    check_input_data(function_coefficients, matrix_A, vector_B,
                     problem_type, signs_vector, non_negative_constraints)

    signs_vector = signs_vector[:]
    # convert to min problem
    if problem_type == problem_types[1]:
        function_coefficients =\
            _negate_vector(function_coefficients)
    # make all variables non negative
    function_coefficients, matrix_A =\
        _all_variables_non_negative(
            function_coefficients, matrix_A, non_negative_constraints)
    # make RHS values non negative
    matrix_A, signs_vector, vector_B = _make_RHS_non_negative(
        matrix_A, signs_vector, vector_B)
    # convert all inequalities to equations
    function_coefficients, matrix_A, signs_vector =\
        _make_all_constraints_equations(
            function_coefficients, matrix_A, signs_vector)

    # convert to big M method form
    function_coefficients, matrix_A = _convert_to_big_M_form(
        function_coefficients, matrix_A)

    return function_coefficients, matrix_A, vector_B


def _add_new_variable_for_non_negativity(
        index, function_coefficients, matrix_A):
    function_coefficients.insert(index + 1, -function_coefficients[index])

    for i, row in enumerate(iter(matrix_A)):
        row.insert(index+1, -matrix_A[i][index])

    return function_coefficients, matrix_A


def _negate_vector(vector):
    return [-x for x in vector]


def _all_variables_non_negative(
        function_coefficients, matrix_A, non_negative_constraints):

    offset = 0
    for index, variable in enumerate(iter(non_negative_constraints)):
        if variable is False:

            function_coefficients, matrix_A =\
                _add_new_variable_for_non_negativity(
                    index+offset, function_coefficients, matrix_A)
            offset += 1

    return function_coefficients, matrix_A


def _make_RHS_non_negative(matrix_A, signs_vector, vector_B):
    for index in range(len(vector_B)):
        if vector_B[index] < 0:

            vector_B[index] = -vector_B[index]
            matrix_A[index] = _negate_vector(matrix_A[index])

            if signs_vector[index] == signs[0]:
                signs_vector[index] = signs[2]
            elif signs_vector[index] == signs[2]:
                signs_vector[index] = signs[0]

    return matrix_A, signs_vector, vector_B


def _make_all_constraints_equations(
        function_coefficients, matrix_A, signs_vector):
    # print(function_coefficients,matrix_A, signs_vector)

    for index, sign in enumerate(iter(signs_vector)):
        pass
        if sign in (signs[0], signs[2]):
            function_coefficients.append(0)
            matrix_A = [matrix_A[i] + [0] for i in range(len(matrix_A))]
            signs_vector[index] = signs[1]
        if sign == signs[0]:
            matrix_A[index][-1] = 1
        elif sign == signs[2]:
            matrix_A[index][-1] = -1
    return function_coefficients, matrix_A, signs_vector


def _convert_to_big_M_form(function_coefficients, matrix_A):
    rows_need_artificial_variable =\
        _rows_need_artificial_variable(function_coefficients, matrix_A)

    for row_index in rows_need_artificial_variable:
        function_coefficients.append(big_M)
        for i, row in enumerate(iter(matrix_A)):
            if i == row_index:
                row.append(1)
                continue
            row.append(0)

    return function_coefficients, matrix_A


def _rows_need_artificial_variable(function_coefficients, matrix_A):
    rows_need_artificial_variable = [i for i in range(len(matrix_A))]

    for j in range(len(function_coefficients)):

        column_vector = [matrix_A[i][j] for i in range(len(matrix_A))]
        found_single_positive_value = False

        for index, value in enumerate(iter(column_vector)):
            if value < 0:
                found_single_positive_value = False
                break
            elif value > 0:
                if found_single_positive_value:
                    found_single_positive_value = False
                    break
                found_single_positive_value = True
                row_of_positive_value = index
            elif value == 0:
                continue
        if found_single_positive_value and(
                row_of_positive_value in rows_need_artificial_variable):
                    rows_need_artificial_variable.remove(row_of_positive_value)

    return rows_need_artificial_variable
