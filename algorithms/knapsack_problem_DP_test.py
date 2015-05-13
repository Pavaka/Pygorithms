import unittest
from knapsack_problem_DP import *


class TestKnapsackDPoptimality(unittest.TestCase):

    def test_knapsack_optimal_solution_exmp1(self):
        items = [(3, 4), (2, 3), (4, 2), (4, 3)]
        capacity = 6
        answer = knapsack_problem_DP(items, capacity)
        self.assertEqual(answer, 8)

    def test_knapsack_optimal_solution_exmp2(self):
        items = [(1, 1), (6, 2), (18, 5), (22, 6), (28, 7)]
        capacity = 11
        answer = knapsack_problem_DP(items, capacity)
        self.assertEqual(answer, 40)

    def test_knapsack_optimal_solution_exmp3(self):
        items = [(1, 1), (6, 2), (18, 4.6), (22, 5.2), (28, 6.4)]
        capacity = 11.5
        answer = knapsack_problem_DP(items, capacity)
        self.assertEqual(answer, 40)


class TestKnapsackDPException(unittest.TestCase):

    def test_negative_capacity(self):
        items = [(3, 4), (2, 3), (4, 2), (4, 3)]
        capacity = -6
        with self.assertRaises(NegativeCapacityError):
            knapsack_problem_DP(items, capacity)

    def test_item_with_non_pisitive_weight(self):
        items = [(3, 4), (2, 3), (4, -2), (4, -3)]
        capacity = 6
        with self.assertRaises(ItemWithNonPositiveWeightError):
            knapsack_problem_DP(items, capacity)

    def test_capacity_NaN(self):
        items = [(3, 4), (2, 3), (4, 2), (4, 3)]
        capacity = "Error"
        with self.assertRaises(TypeError):
            knapsack_problem_DP(items, capacity)

    def test_weight_NaN(self):
        items = [(3, "four"), (2, 3), (4, 2), (4, 3)]
        capacity = 6
        with self.assertRaises(TypeError):
            knapsack_problem_DP(items, capacity)

    def test_value_NaN(self):
        items = [(3, 4), ("two", 3), (4, 2), (4, 3)]
        capacity = 6
        with self.assertRaises(TypeError):
            knapsack_problem_DP(items, capacity)

    def test_items_not_a_list(self):
        items = 3
        capacity = 6
        with self.assertRaises(TypeError):
            knapsack_problem_DP(items, capacity)

    def test_item_with_non_positive_value(self):
        items = [(3, 4), (-2, 3), (4, 2), (4, 3)]
        capacity = 5
        with self.assertRaises(ItemWithNonPositiveValueError):
            knapsack_problem_DP(items, capacity)


if __name__ == '__main__':
    unittest.main()
