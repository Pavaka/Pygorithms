import unittest
import sys
import os
path = os.path.abspath("../algorithms")
sys.path.append(path)
import knapsack_problem_DP as KPDP


class TestKnapsackDPoptimality(unittest.TestCase):

    def test_knapsack_optimal_solution_exmp1(self):
        items = [(3, 4), (2, 3), (4, 2), (4, 3)]
        capacity = 6
        answer = KPDP.knapsack_problem_DP(items, capacity)
        self.assertEqual(answer, 8)

    def test_knapsack_optimal_solution_exmp2(self):
        items = [(1, 1), (6, 2), (18, 5), (22, 6), (28, 7)]
        capacity = 11
        answer = KPDP.knapsack_problem_DP(items, capacity)
        self.assertEqual(answer, 40)

    def test_knapsack_optimal_solution_exmp3(self):
        items = [(1, 1), (6, 2), (18, 5), (22, 6), (28, 7)]
        capacity = 0
        answer = KPDP.knapsack_problem_DP(items, capacity)
        self.assertEqual(answer, 0)

    def test_knapsack_optimal_solution_exmp4(self):
        items = []
        capacity = 15
        answer = KPDP.knapsack_problem_DP(items, capacity)
        self.assertEqual(answer, 0)


if __name__ == '__main__':
    unittest.main()
