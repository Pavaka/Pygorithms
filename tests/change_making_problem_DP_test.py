import unittest
import sys
import os
path = os.path.abspath("../pygorithms")
sys.path.append(path)
import change_making_problem_DP as CMP_DP


class TestCMPOptimality(unittest.TestCase):

    def test_CMP_optimality_exmp1(self):
        coin_denominations = [1, 5, 6, 8]
        money_amount = 11
        answer = CMP_DP.change_making_problem_DP(
            coin_denominations, money_amount)
        self.assertEqual(answer, [6, 5])

    def test_CMP_optimality_exmp2(self):
        coin_denominations = [1, 3, 5, 12, 48]
        money_amount = 15
        answer = CMP_DP.change_making_problem_DP(
            coin_denominations, money_amount)
        self.assertEqual(answer, [12, 3])


class TestCMPExceptions(unittest.TestCase):

    def test_no_solution_error(self):
        coin_denominations = [2, 4, 8]
        money_amount = 31
        with self.assertRaises(CMP_DP.NoFeasibleSolutionError):
            CMP_DP.change_making_problem_DP(coin_denominations, money_amount)


if __name__ == '__main__':
    unittest.main()

