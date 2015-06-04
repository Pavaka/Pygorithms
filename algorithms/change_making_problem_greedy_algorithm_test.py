import unittest
import change_making_problem_greedy_algorithm


class TestCoinsSolution(unittest.TestCase):

    def test_coins_solution_exmp1(self):
        coin_denominations = [3, 8, 12]
        money_amount = 27

        solution = change_making_problem_greedy_algorithm.change_making_problem_greedy_algorithm(coin_denominations, money_amount)

        self.assertEqual(solution, [12, 12, 3])

if __name__ == '__main__':
    unittest.main()
