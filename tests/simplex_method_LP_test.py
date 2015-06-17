import unittest
import sys
import os
path = os.path.abspath("..")
sys.path.append(path)
from algorithms import simplex_method_LP as SMLP


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
        optimal_solution = SMLP._get_optimal_solution(self.simplex_table)
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



class TestSimplexMethod(unittest.TestCase):

    def setUp(self):
        self.m = 100
        self.function_coefficients = [-3, -1, 1, 0, 0, 0]
        self.matrix_A = [[-2, 1, -1, 1, 0, 0],
                         [1, -1, 1, 0, 1, 0],
                         [3, 1, -1, 0, 0, 1]]
        self.Xb = SMLP._calculate_Xb(self.matrix_A)
        self.Cb = SMLP._calculate_Cb(self.function_coefficients, self.Xb)
        self.simplex_table = SMLP.SimplexTable(self.function_coefficients, self.Xb, self.Cb)
        self.simplex_table.core_table = self.matrix_A
        self.simplex_table.B_slash = [4, 2, 22]
        self.simplex_table.C_slash = SMLP._calculate_C_slash(self.simplex_table)

    def test_calc_Xb(self):
        self.assertEqual(self.simplex_table.Xb, [3, 4, 5])

    def test_calc_Cb(self):
        self.assertEqual(self.simplex_table.Cb, [0, 0, 0])

    def test_calc_C_slash(self):

        C_slash = [-3, -1, 1, 0, 0, 0, 0]
        self.assertEqual(self.simplex_table.C_slash, C_slash)

    def test_key_element(self):
        key_element = SMLP._find_key_element(self.simplex_table)
        self.assertEqual(key_element[0], 1)
        self.assertEqual(key_element[1], [4, 0])
        self.assertEqual(key_element[2], (1, 0))

    def test_new_simplex_table(self):
        new_simplex_table = SMLP._new_simplex_table(self.simplex_table)


if __name__ == '__main__':
    unittest.main()
