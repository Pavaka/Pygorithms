import unittest
import sys
import os
path = os.path.abspath("../input_checkers")
sys.path.append(path)
from TP_input_checker import *


class TestTPInputChecker(unittest.TestCase):

    def setUp(self):
        self.costs = [i for i in range(1, 13)]
        self.vector_a = [100, 130, 200]
        self.vector_b = [150, 120, 80, 50]

    def test_empty_list(self):
        self.costs = []
        with self.assertRaises(EmptyListError):
            check_input_data(self.costs, self.vector_a, self.vector_b)

    def test_vector_a_not_list(self):
        self.vector_a = 5
        with self.assertRaises(VectorANotListError):
            check_input_data(self.costs, self.vector_a, self.vector_b)

    def test_vector_b_not_list(self):
        self.vector_b = "bs"
        with self.assertRaises(VectorBNotListError):
            check_input_data(self.costs, self.vector_a, self.vector_b)

    def test_costs_not_list(self):
        self.costs = print
        with self.assertRaises(CostsNotListError):
            check_input_data(self.costs, self.vector_a, self.vector_b)

    def test_list_contains_NaN(self):
        self.vector_a = [1, 2, "Spad"]
        with self.assertRaises(ListContainsNaN):
            check_input_data(self.costs, self.vector_a, self.vector_b)

    def test_negative_value_in_list(self):
        self.costs = [1, 2, -5]
        with self.assertRaises(NegativeValueError):
            check_input_data(self.costs, self.vector_a, self.vector_b)


if __name__ == '__main__':
    unittest.main()
