import unittest
import sys
import os
path = os.path.abspath("..")
sys.path.append(path)
from algorithms import simplex_LP_covnert_to_trivial_starting_verticie_form as CF


class TestSmallerFunctions(unittest.TestCase):

    def setUp(self):

        self.function_coefficients = [5, 7, -13, 18, -26]
        self.matrix_A = [[3, 5, 0, -16, 0],
                         [-6, 0, -1, 1, -1],
                         [5, 0, -7, 1, -1]]
        self.vector_B = [2, -7, -6]
        self.problem_type = "max"
        self.signs_vector = ["le", "eq", "ge"]
        self.non_negative_constraints = [False, True, False, True, False]

    def test_add_variable_for_non_negativity(self):
        index = self.non_negative_constraints.index(False, 0)

        function_coefficients, matrix_A =\
            CF._add_new_variable_for_non_negativity(
                index, self.function_coefficients, self.matrix_A)

        self.assertEqual(function_coefficients, [5, -5, 7, -13, 18, -26])
        self.assertEqual(matrix_A, [[3, -3, 5, 0, -16, 0],
                                    [-6, 6, 0, -1, 1, -1],
                                    [5, -5, 0, -7, 1, -1]])

    def test_all_variables_non_negative(self):
        function_coefficients, matrix_A =\
            CF._all_variables_non_negative(
                self.function_coefficients, self.matrix_A, self.non_negative_constraints)

        self.assertEqual(
            function_coefficients, [5, -5, 7, -13, 13, 18, -26, 26])

        self.assertEqual(matrix_A, [[3, -3, 5, 0, 0, -16, 0, 0],
                                    [-6, 6, 0, -1, 1, 1, -1, 1],
                                    [5, -5, 0, -7, 7, 1, -1, 1]])


    def test_make_RHS_non_negative(self):

        matrix_A, signs_vector, vector_B =\
            CF._make_RHS_non_negative(
                self.matrix_A, self.signs_vector, self.vector_B)

        self.assertEqual(matrix_A, [[3, 5, 0, -16, 0],
                                    [6, 0, 1, -1, 1],
                                    [-5, 0, 7, -1, 1]])
        self.assertEqual(vector_B, [2, 7, 6])
        self.assertEqual(signs_vector, ["le", "eq", "le"])

    def test_make_all_constraints_equations(self):
        function_coefficients, matrix_A, signs_vector = CF._make_all_constraints_equations(self.function_coefficients, self.matrix_A, self.signs_vector)
        self.assertEqual(function_coefficients, [5, 7, -13, 18, -26, 0, 0])
        self.assertEqual(matrix_A, [[3, 5, 0, -16, 0, 1, 0],
                                    [-6, 0, -1, 1, -1, 0, 0],
                                    [5, 0, -7, 1, -1, 0, -1]])

    def test_rows_need_artificial_variable(self):
        rows_need_artificial_variable = CF._rows_need_artificial_variable(self.function_coefficients, self.matrix_A)
        self.assertEqual(rows_need_artificial_variable, [1, 2])
        self.matrix_A[0][1] = 0
        rows_need_artificial_variable = CF._rows_need_artificial_variable(self.function_coefficients, self.matrix_A)
        self.assertEqual(rows_need_artificial_variable, [0, 1, 2])
if __name__ == '__main__':
    unittest.main()
