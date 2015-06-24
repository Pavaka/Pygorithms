import unittest
import sys
import os
path = os.path.abspath("../pygorithms")
sys.path.append(path)
import change_making_problem_greedy_algorithm as CMP_greedy


class TestCoinsSolution(unittest.TestCase):

    def test_coins_solution_exmp1(self):
        coin_denominations = [3, 8, 12]
        money_amount = 27
        answer = CMP_greedy.change_making_problem_greedy_algorithm(
            coin_denominations, money_amount)
        self.assertEqual(answer, [12, 12, 3])

    def test_coins_solution_exmp2(self):
        coin_denominations = [1, 3, 5, 12, 48]
        money_amount = 9
        answer = CMP_greedy.change_making_problem_greedy_algorithm(
            coin_denominations, money_amount)
        self.assertEqual(answer, [5, 3, 1])

    def test_coins_solution_exmp3(self):
        coin_denominations = [1, 3, 5, 12, 15]
        money_amount = 55
        answer = CMP_greedy.change_making_problem_greedy_algorithm(
            coin_denominations, money_amount)
        self.assertEqual(answer, [15, 15, 15, 5, 5])


class TestCoinsExceptions(unittest.TestCase):

    def test_no_feasible_solution_error(self):
        coin_denominations = [2, 4, 8]
        money_amount = 31
        with self.assertRaises(CMP_greedy.NoFeasibleSolutionError):
            CMP_greedy.change_making_problem_greedy_algorithm(
                coin_denominations, money_amount)

if __name__ == '__main__':
    unittest.main()
