def knapsack_problem_DP(items, capacity):
    """Given a list of items (each item is a two-tuple), where every item has a
    value and weight, finds the highest value that can be
    achieved from a subset of the items subject to the constraint
    of the capacity.
"""
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

    return knapsack_table[number_of_items][capacity]
