import unittest
from knapsack_problem_DP import knapsack_problem_DP


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


if __name__ == '__main__':
    unittest.main()
