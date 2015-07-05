import unittest
import sys
import os
path = os.path.abspath("../input_checkers")
sys.path.append(path)
from SM_input_checker import *


class TestCheckInptutData(unittest.TestCase):

    def setUp(self):
        self.function_coefficients = [-5, 2]
        self.matrix_A = [[1, -1],
                         [1, -2],
                         [2, -1]]
        self.vector_B = [2, 0, 1]
        self.problem_type = "min"
        self.non_negative_constraints = [True, False]
        self.signs_vector = ["ge", "ge", "le"]
        self.args = [self.function_coefficients, self.matrix_A,
                     self.vector_B, self.problem_type,
                     self.non_negative_constraints,
                     self.signs_vector]

    def test_func_coef_type_error(self):
        self.args[0] = "not a list"
        with self.assertRaises(FuncCoefTypeError):
            check_input_data(*self.args)

    def test_matrixA_type_error(self):
        self.args[1] = "not a list"
        with self.assertRaises(MatrixATypeError):
            check_input_data(*self.args)

    def test_vector_B_type_error(self):
        self.args[2] = "not a list"
        with self.assertRaises(VectorBTypeError):
            check_input_data(*self.args)

    def test_signs_vector_type_error(self):
        self.args[4] = "not a list"
        with self.assertRaises(SignsVectorTypeError):
            check_input_data(*self.args)

    def test_non_negative_constr_type_error(self):
        self.args[5] = "not a list"
        with self.assertRaises(NonNegativeConstraintTypeError):
            check_input_data(*self.args)

    def test_problem_type_error(self):
        self.args[3] = "not a min thingie"
        with self.assertRaises(ProblemTypeValueError):
            check_input_data(*self.args)


if __name__ == '__main__':
    unittest.main()
