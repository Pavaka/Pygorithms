import unittest
import sys
import os
path = os.path.abspath("../input_checkers")
sys.path.append(path)
from KP_input_chekcer import *


class TestKPInputChecker(unittest.TestCase):

    def test_negative_capacity(self):
        items = [(3, 4), (2, 3), (4, 2), (4, 3)]
        capacity = -6
        with self.assertRaises(NegativeCapacityError):
            check_input_data(items, capacity)

    def test_item_with_non_pisitive_weight(self):
        items = [(3, 4), (2, 3), (4, -2), (4, -3)]
        capacity = 6
        with self.assertRaises(ItemWithNegativeWeightError):
            check_input_data(items, capacity)

    def test_capacity_NaN(self):
        items = [(3, 4), (2, 3), (4, 2), (4, 3)]
        capacity = "Error"
        with self.assertRaises(CapacityNotAnIntegerError):
            check_input_data(items, capacity)

    def test_weight_NaN(self):
        items = [(3, "four"), (2, 3), (4, 2), (4, 3)]
        capacity = 6
        with self.assertRaises(InvalidItemError):
            check_input_data(items, capacity)

    def test_value_NaN(self):
        items = [(3, 4), ("two", 3), (4, 2), (4, 3)]
        capacity = 6
        with self.assertRaises(InvalidItemError):
            check_input_data(items, capacity)

    def test_items_not_a_list(self):
        items = 3
        capacity = 6
        with self.assertRaises(ItemsNotAListOrTupleError):
            check_input_data(items, capacity)

    def test_item_with_non_positive_value(self):
        items = [(3, 4), (-2, 3), (4, 2), (4, 3)]
        capacity = 5
        with self.assertRaises(
                               ItemWithNegativeValueError):
            check_input_data(items, capacity)

    def test_item_three_tuple(self):
        items = [(3, 4), (2, 3), (4, 2), (4, 3, 7)]
        capacity = 6
        with self.assertRaises(InvalidItemError):
            check_input_data(items, capacity)

    def test_negative_value_item_error(self):
        items = [(45, 3), (30, 5), (-45, 9), (10, 5)]
        capacity = 1
        with self.assertRaises(
                               ItemWithNegativeValueError):
            check_input_data(items, capacity)

    def test_negative_weight_item_error(self):
        items = [(45, 3), (30, 5), (45, 9), (10, -5)]
        capacity = 1
        with self.assertRaises(
                               ItemWithNegativeWeightError):
            check_input_data(items, capacity)

    def test_invalid_items_exmp_1(self):
        items = "Items"
        capacity = 1
        with self.assertRaises(ItemsNotAListOrTupleError):
            check_input_data(items, capacity)

    def test_invalid_items_exmp_2(self):
        items = [(45, 3), 3, (45, 9), (10, 5)]
        capacity = 1
        with self.assertRaises(InvalidItemError):
            check_input_data(items, capacity)

    def test_invalid_capacity(self):
        items = [(45, 3), 3, (45, 9), (10, 5)]
        capacity = "This is not capacity"
        with self.assertRaises(CapacityNotAnIntegerError):
            check_input_data(items, capacity)


if __name__ == '__main__':
    unittest.main()
