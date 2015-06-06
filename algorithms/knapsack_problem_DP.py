from input_checkers.KP_input_chekcer import *


def knapsack_problem_DP(items, capacity):
    """Given a list of items (each item is a two-tuple with numbers
    (value, weight)), where every item has a value and weight ,
    finds the highest value that can be
    achieved from a subset of the items subject to the constraint
    of the capacity (the sum of all included items must be
    less than or equal to the capacity).


    Since list and tuple behave in the same way with respect to
    indexing the function can work with tuples and lists for items,
    and each item can be a two-tuple or list of size 2.

    Weights and capacity have to be positive integers.
    If capacity is fraction it is rounded to the closest integer
    below it. If item weight is fraction it is rounded to the closes
    integer that is higher.

    The function returns a single integer value that represents the
    optimal value.

    The problem is solved using dynamic programming approach.
    """
    _check_input_data(items, capacity)

    number_of_items = len(items)

    knapsack_table = [[0 for x in range(capacity + 1)]
                      for x in range(number_of_items + 1)]

    for index, item in enumerate(iter(items)):
        index += 1

        item_value = item[0]
        item_weight = item[1]

        for current_max_capacity in range(capacity + 1):
            i = index
            w = current_max_capacity
            if current_max_capacity < item_weight:
                knapsack_table[i][w] = knapsack_table[i - 1][w]
            else:
                knapsack_table[i][w] = max(knapsack_table[i - 1][w],
                                           knapsack_table[i - 1]
                                           [w - item_weight] + item_value)
    optimal_value = knapsack_table[number_of_items][capacity]
    return optimal_value
