import unittest
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

    def test_money_amount_not_integer(self):
        coin_denominations = [1, 3, 5, 12, 48]
        money_amount = "Money amount"
        with self.assertRaises(CMP_greedy.MoneyAmountNotAnIntegerError):
            CMP_greedy.change_making_problem_greedy_algorithm(
                coin_denominations, money_amount)

    def test_money_amount_non_positive(self):
        coin_denominations = [1, 3, 5, 12, 48]
        money_amount = 0
        with self.assertRaises(CMP_greedy.NonPositiveMoneyAmountError):
            CMP_greedy.change_making_problem_greedy_algorithm(
                coin_denominations, money_amount)

    def test_coin_denominations_not_list_tuple(self):
        coin_denominations = {"one": 1}
        money_amount = 15
        with self.assertRaises(
                CMP_greedy.CoinDenominationsNotAListOrTupleError):
                    CMP_greedy.change_making_problem_greedy_algorithm(
                        coin_denominations, money_amount)

    def test_coin_denomination_not_integer(self):
        coin_denominations = [1, 3, 5, "This is not an integer", 48]
        money_amount = 15
        with self.assertRaises(CMP_greedy.CoinDenominationNotAnIntegerError):
            CMP_greedy.change_making_problem_greedy_algorithm(
                coin_denominations, money_amount)

    def test_coin_denomination_negative_int(self):
        coin_denominations = [1, 3, -5, 16, 48]
        money_amount = 15
        with self.assertRaises(CMP_greedy.CoinDenominationNonPositiveError):
            CMP_greedy.change_making_problem_greedy_algorithm(
                coin_denominations, money_amount)

if __name__ == '__main__':
    unittest.main()
