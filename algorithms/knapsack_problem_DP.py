from math import floor, ceil


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
"""
    if capacity < 0:
        raise NegativeCapacityError

    capacity = floor(capacity)

    number_of_items = len(items)
    knapsack_table = [[0 for x in range(capacity + 1)]
                      for x in range(number_of_items + 1)]

    for index, item in enumerate(iter(items)):
        index += 1

        item_value = item[0]
        item_weight = ceil(item[1])

        if item_weight <= 0:
            raise ItemWithNonPositiveWeightError

        for current_max_capacity in range(capacity + 1):
            i = index
            w = current_max_capacity
            if current_max_capacity < item_weight:
                knapsack_table[i][w] = knapsack_table[i - 1][w]
            else:
                knapsack_table[i][w] = max(knapsack_table[i - 1][w],
                                           knapsack_table[i - 1]
                                           [w - item_weight] + item_value)

    return knapsack_table[number_of_items][capacity]


class NegativeCapacityError(Exception):
    pass


class ItemWithNonPositiveWeightError(Exception):
    pass
