def knapsack_problem_DP(items, capacity):
    """Given a list of items (each item is a two-tuple (value, weight)),
    where every item has a value and weight , 
    finds the highest value that can be
    achieved from a subset of the items subject to the constraint
    of the capacity.
    Since list and tuple behave in the same way with respect to
    indexing the function can work with tuples and lists for items,
    and each item can be a two-tuple or list of size 2.
"""
    if capacity < 0:
        raise NegativeCapacityError

    if not isinstance(items, (list, tuple)):
        raise ItemsNotATupleOrListError

    number_of_items = len(items)
    knapsack_table = [[0 for x in range(capacity + 1)]
                      for x in range(number_of_items + 1)]

    for index, item in enumerate(iter(items)):
        index += 1

        try:
            item_value = item[0]
            item_weight = item[1]
        except TypeError:
            raise ItemNotATwoTuple

        try:
            item[2]
        except:
            pass
        else:
            raise ItemNotATwoTuple

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


class ItemsNotATupleOrListError(Exception):
    pass


class ItemWithNonPositiveWeightError(Exception):
    pass


class ItemNotATwoTuple(Exception):
    pass
