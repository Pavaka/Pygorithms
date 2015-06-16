import unittest
import sys
import os
path = os.path.abspath("..")
sys.path.append(path)
# from algorithms.simplex_method_LP import *
from algorithms import simplex_method_LP as SMLP

class TestFindStartingVertex(unittest.TestCase):

    def test_find_starting_vertex(self):
        matrix_A = [[1, 1, 0, 0, -1, 0, 1],
                    [0, 1, 0, 0, 0, 1, 0],
                    [1, -2, -1, 1, 0, 0, 0]]
        result = SMLP._find_starting_vertex(matrix_A)
        self.assertEqual(result, [3, 5, 6])

class TestCalculateCSlash(unittest.TestCase):

    def setUp(self):
        self.function_coefficients = [-3, -1, 1, 0, 0, 0]
        self.Xb = [3, 4, 5]
        self.Cb = [1, 2, 3]
        self.simplex_table = SMLP.SimplexTable(self.function_coefficients, self.Xb, self.Cb)
        self.simplex_table.core_table = [[-2, 1, -1, 1, 0, 0],
                                        [1, -1, 1, 0, 1, 0],
                                        [3, 1, -1, 0, 0, 1]]
        self.simplex_table.B_slash = [4, 2, 22]
        
    def test_calculate_C_slash(self):
        self.simplex_table.C_slash = SMLP._calculate_C_slash(self.simplex_table)
        expected_result = [-12, -3, 3, -1, -2, -3, -74]
        self.assertEqual(self.simplex_table.C_slash, expected_result)




if __name__ == '__main__':
    unittest.main()
