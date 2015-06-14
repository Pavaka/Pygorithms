import sys
import os
sys.path.append(os.path.abspath(".."))
from input_checkers.CMP_input_checker import *


def change_making_problem_DP(coin_denominations, money_amount):

    _check_input_data(coin_denominations, money_amount)

    coin_denominations = sorted(coin_denominations)
    DP_table = [[0 for _ in range(money_amount + 1)]
                for _ in range(len(coin_denominations))]
    DP_table_columns = len(DP_table[0])
    DP_table_rows = len(DP_table)
    for index in range(DP_table_columns):
        DP_table[0][index] = index/coin_denominations[0]

    for index, coin in enumerate(iter(coin_denominations[1:])):
        index += 1
        for current_money_amount in range(1, DP_table_columns):
            i = index
            j = current_money_amount
            if j < coin_denominations[i]:
                DP_table[i][j] = DP_table[i - 1][j]
            else:

                upper_cell = DP_table[i - 1][j]
                lefter_cell = DP_table[i][j - coin_denominations[i]]

                upper_cell_is_integer = False
                lefter_cell_is_integer = False

                if upper_cell % 1 == 0:
                    upper_cell_is_integer = True

                if lefter_cell % 1 == 0:
                    lefter_cell_is_integer = True

                if not (upper_cell_is_integer ^ lefter_cell_is_integer):
                    DP_table[i][j] = min(upper_cell, lefter_cell + 1)
                else:
                    if upper_cell_is_integer:
                        DP_table[i][j] = upper_cell
                    else:
                        DP_table[i][j] = lefter_cell + 1

    optimal_number_coins = DP_table[-1][-1]
    if optimal_number_coins % 1 != 0:
        raise NoFeasibleSolutionError

    i = DP_table_rows - 1
    j = DP_table_columns - 1
    optimal_solution = []
    while True:
        coins_left = DP_table[i][j]

        if coins_left == 0:
            return optimal_solution

        if coins_left == DP_table[i - 1][j]:
            i -= 1
        else:
            j -= coin_denominations[i]
            optimal_solution.append(coin_denominations[i])
    # return optimal_number_coins


def _check_input_data(coin_denominations, money_amount):
    pass


class NoFeasibleSolutionError(Exception):
    pass
