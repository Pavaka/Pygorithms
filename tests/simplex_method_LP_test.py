import unittest
import sys
import os
path = os.path.abspath("..")
sys.path.append(path)
from pygorithms import simplex_method_LP as SMLP


class TestSmallerFunctions(unittest.TestCase):

    def setUp(self):
        self.function_coefficients = [7, 3, -1, 1, 0, 100]
        self.matrix_A = [[3, 3, 0, 0, -1, 1],
                         [1, -3, -1, 1, 0, 0]]
        self.Xb = SMLP._calculate_Xb(self.matrix_A)
        self.Cb = SMLP._calculate_Cb(self.function_coefficients, self.Xb)
        self.simplex_table = SMLP.SimplexTable(
            self.function_coefficients, self.Xb, self.Cb)
        self.simplex_table.core_table = self.matrix_A
        self.simplex_table.B_slash = [4, 6]
        self.simplex_table.C_slash = SMLP._calculate_C_slash(
            self.simplex_table)

    def test_calculate_Xb(self):
        Xb = SMLP._calculate_Xb(self.matrix_A)
        self.assertEqual(Xb, [5, 3])

    def test_calculate_Cb(self):
        Xb = SMLP._calculate_Xb(self.matrix_A)
        Cb = SMLP._calculate_Cb(self.function_coefficients, Xb)
        self.assertEqual(Cb, [100, 1])

    def test_calculate_C_slash(self):
        C_slash = SMLP._calculate_C_slash(self.simplex_table)
        self.assertEqual(C_slash, [-294, -294, 0, 0, 100, 0, -406])

    def test_get_optimal_solution(self):
        optimal_solution = SMLP._get_optimal_solution(self.simplex_table, "min",[True] * 6, ["eq"] * 2)
        self.assertEqual(optimal_solution[0], 406)
        self.assertEqual(optimal_solution[1], [0, 0, 0, 6, 0, 4])

    def test_check_simplex_table_optimality_status_2(self):
        optimality = SMLP._check_simplex_table_optimality(self.simplex_table)
        self.assertEqual(SMLP.simplex_table_statuses[2], optimality)

    def test_check_simplex_table_optimality_status_1(self):
        self.simplex_table.core_table[1][0] = -5
        optimality = SMLP._check_simplex_table_optimality(self.simplex_table)
        self.assertEqual(SMLP.simplex_table_statuses[1], optimality)

    def test_check_simplex_table_optimality_status_0(self):
        self.simplex_table.C_slash[0] = 5
        self.simplex_table.C_slash[1] = 10
        optimality = SMLP._check_simplex_table_optimality(self.simplex_table)
        self.assertEqual(SMLP.simplex_table_statuses[0], optimality)

    def test_find_key_element_exmp1(self):
        key_element = SMLP._find_key_element(self.simplex_table)
        self.assertEqual(key_element[0], 3)
        self.assertEqual(key_element[1], [5, 0])



class TestSimplexMethodSteps(unittest.TestCase):

    def setUp(self):
        self.m = 100
        self.function_coefficients = [7, 3, -1, 1, 0, self.m]
        self.matrix_A = [[3, 3, 0, 0, -1, 1],
                         [1, -3, -1, 1, 0, 0]]
        self.vector_B = [4, 6]
        self.Xb = SMLP._calculate_Xb(self.matrix_A)
        self.Cb = SMLP._calculate_Cb(self.function_coefficients, self.Xb)
        self.simplex_table = SMLP.SimplexTable(self.function_coefficients, self.Xb, self.Cb)
        self.simplex_table.core_table = self.matrix_A
        self.simplex_table.B_slash = [4, 6]
        self.simplex_table.C_slash = SMLP._calculate_C_slash(self.simplex_table)

    def test_calc_Xb(self):
        self.assertEqual(self.simplex_table.Xb, [5, 3])

    def test_calc_Cb(self):
        self.assertEqual(self.simplex_table.Cb, [self.m, 1])

    def test_calc_C_slash(self):

        C_slash = [6- 3*self.m, 6 -3*self.m, 0, 0, self.m, 0, -6 - 4*self.m]
        self.assertEqual(self.simplex_table.C_slash, C_slash)

    def test_key_element(self):
        key_element = SMLP._find_key_element(self.simplex_table)
        self.assertEqual(key_element[0], 3)
        self.assertEqual(key_element[1], [5, 0])
        self.assertEqual(key_element[2], (0, 0))

    def test_new_simplex_table(self):
        two = 1.9999999999999998
        new_simplex_table = SMLP._new_simplex_table(self.simplex_table)
        new_core_table = [[1, 1, 0, 0, -1/3, 1/3],
                          [0, -4, -1, 1, 1/3, -1/3]]
        self.assertEqual(new_simplex_table.core_table, new_core_table)
        self.assertEqual(new_simplex_table.B_slash, [4/3, 14/3])
        new_C_slash = [0, 0, 0, 0, two, -2+self.m, -14]
        self.assertEqual(new_simplex_table.C_slash,new_C_slash)

    def test_simplex_method(self):
        solution = SMLP.simplex_method(self.function_coefficients, self.matrix_A, self.vector_B)
        self.assertEqual(solution[0], 14)
        self.assertEqual(solution[1], [4/3, 0, 0, 14/3, 0, 0])


class TestSimplexMethodTestExamples(unittest.TestCase):

    def test_simplex_method_exmp1(self):
        m = 100
        function_coefficients = [-2, 7, 3, -3, 0, 0, m]
        matrix_A = [[1, 1, 0, 0, -1, 0, 1],
                    [0, 1, 0, 0, 0, 1, 0],
                    [1, -2, -1, 1, 0, 0, 0]]
        vector_B = [2, 4, 3]
        solution = SMLP.simplex_method(function_coefficients, matrix_A, vector_B)
        self.assertEqual(solution[0], -7)
        self.assertEqual(solution[1], [2, 0, 0, 1, 0, 4, 0])

    def test_simplex_method_exmp2(self):
        function_coefficients = [1, 1]
        matrix_A = [[1, 1], [1, -2]]
        vector_B = [-1, 2]
        problem_type = "max"
        signs_vector = ["le", "le"]
        non_negative_constraints = [False, True]
        solution = SMLP.simplex_method(function_coefficients,
            matrix_A, vector_B, problem_type, signs_vector,
            non_negative_constraints)
        self.assertEqual(solution[0], -1)
        self.assertEqual(solution[1], [-1, 0])

if __name__ == '__main__':
    unittest.main()
