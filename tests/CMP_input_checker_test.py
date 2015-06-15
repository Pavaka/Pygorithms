import unittest
import sys
import os
path = os.path.abspath("../input_checkers")
sys.path.append(path)
from CMP_input_checker import *


class TestCMPInputChecker(unittest.TestCase):

    def test_money_amount_not_integer(self):
        coin_denominations = [1, 3, 5, 12, 48]
        money_amount = "Money amount"
        with self.assertRaises(MoneyAmountNotAnIntegerError):
            check_input_data(coin_denominations, money_amount)

    def test_money_amount_non_positive(self):
        coin_denominations = [1, 3, 5, 12, 48]
        money_amount = 0
        with self.assertRaises(NonPositiveMoneyAmountError):
            check_input_data(coin_denominations, money_amount)

    def test_coin_denominations_not_list_tuple(self):
        coin_denominations = {"one": 1}
        money_amount = 15
        with self.assertRaises(
                 CoinDenominationsNotAListOrTupleError):
            check_input_data(coin_denominations, money_amount)

    def test_coin_denomination_not_integer(self):
        coin_denominations = [1, 3, 5, "This is not an integer", 48]
        money_amount = 15
        with self.assertRaises(CoinDenominationNotAnIntegerError):
            check_input_data(coin_denominations, money_amount)

    def test_coin_denomination_negative_int(self):
        coin_denominations = [1, 3, -5, 16, 48]
        money_amount = 15
        with self.assertRaises(CoinDenominationNonPositiveError):
            check_input_data(coin_denominations, money_amount)

    def test_coin_denomination_empty_list(self):
        coin_denominations = []
        money_amount = 15
        with self.assertRaises(EmptyCoinsListError):
            check_input_data(coin_denominations, money_amount)

if __name__ == '__main__':
    unittest.main()
