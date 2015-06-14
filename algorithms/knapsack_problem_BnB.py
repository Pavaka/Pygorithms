import sys
import os
sys.path.append(os.path.abspath(".."))
from input_checkers.KP_input_chekcer import *


class Node:

    """
    A class that represents Node. It is initiallized
    as empty Node and its attributes valeus are changed dynamically.
    """

    def __init__(self):
        self.value = 0
        self.weight = 0
        self.upper_bound = 0
        self.branching_vector = list()

# A number that is assigned to the upper bound in case it is non existent
no_upper_bound_value = -100


def knapsack_problem_BnB(items, capacity):
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

    The function returns a tuple with optimal value and optimal solution
    where optimal value is a positive integer, and optimal solution is a
    list with items with value (0 or 1).

    The problem is solved using branch and bound algorithm that treverses
    through nodes untill it finds the optimal solution.
    """

    _check_input_data(items, capacity)

    items = sorted(items, key=lambda item: item[0]/item[1])[::-1]

    problem_definition = (items, capacity)
    number_of_items = len(items)

    root_node = Node()
    root_node.branching_vector = [None for _ in range(number_of_items)]

    root_node.upper_bound = _calculate_upper_bound(problem_definition,
                                                   root_node)
    live_nodes = [root_node]

    while True:

        highest_upper_bound_node = _get_highest_upper_bound_node(live_nodes)
        found_optimmal_solution = _found_optimal_solution(live_nodes)

        if found_optimmal_solution:
            return (highest_upper_bound_node.value,
                    highest_upper_bound_node.branching_vector)

        branched_node = highest_upper_bound_node

        # Create the new branched nodes
        left_child = Node()
        right_child = Node()
        # Find and assign the branching vector of each child
        branching_vectors = _find_childs_branching_vector(branched_node.
                                                          branching_vector)
        left_child.branching_vector = branching_vectors[0]
        right_child.branching_vector = branching_vectors[1]

        # calculate and assigne left child value weight
        left_child_value_weight = _calculate_value_weight_of_node(
            problem_definition, left_child)
        left_child.value = left_child_value_weight[0]
        left_child.weight = left_child_value_weight[1]

        # calculate and assigne right child value weight
        right_child_value_weight = _calculate_value_weight_of_node(
            problem_definition, right_child)
        right_child.value = right_child_value_weight[0]
        right_child.weight = right_child_value_weight[1]

        # calculate and assigne upper bound of left child
        left_child.upper_bound = _calculate_upper_bound(problem_definition,
                                                        left_child)
        right_child.upper_bound = _calculate_upper_bound(problem_definition,
                                                         right_child)

        # delete the branched node
        live_nodes.remove(branched_node)

        # add child nodes if they have upper bound
        if left_child.upper_bound != no_upper_bound_value:
            live_nodes.append(left_child)
        if right_child.upper_bound != no_upper_bound_value:
            live_nodes.append(right_child)


def _calculate_value_weight_of_node(problem_def, node):
    """
    Function that takes a Node with his branching vector set
    and calculates the value and weight attributes of that Node.
    problem_def is a tuple (items, capacity) which represent the
    original optimizaiton problem.
    """
    items = problem_def[0]
    number_of_items = len(items)
    sub_vercotr = [node.branching_vector[i] for i in
                   range(number_of_items) if node.branching_vector[i] != None]
    value = 0
    weight = 0
    for x in range(len(sub_vercotr)):
        value += sub_vercotr[x]*items[x][0]
        weight += sub_vercotr[x]*items[x][1]
    return value, weight


def _calculate_upper_bound(problem_def, node):
    """
    A function that takes a Node that has his value , weight
    and branching vector set, and calculates the upper bound of that
    node with respect to the problem.
    problem_def is a tuple (items, capacity) which represent the
    original optimizaiton problem.
    """
    items = problem_def[0]
    capacity = problem_def[1]
    upper_bound = node.value
    remaining_capacity = capacity - node.weight
    if remaining_capacity < 0:
        return no_upper_bound_value

    for index, item in enumerate(iter(items)):
        item_value = item[0]
        item_weight = item[1]
        if node.branching_vector[index] is None:
            if remaining_capacity - item_weight >= 0:
                upper_bound += item_value
                remaining_capacity -= item_weight
            else:
                upper_bound += (remaining_capacity/item_weight)*item_value
                return upper_bound

    return upper_bound


def _get_highest_upper_bound_node(live_nodes):
    """
    Function that takes a list of nodes and returns
    the one with the highest upper bound value.
    """
    highest_upper_bound_node = live_nodes[0]
    for node in live_nodes:
        if node.upper_bound > highest_upper_bound_node.upper_bound:
            highest_upper_bound_node = node
    return highest_upper_bound_node


def _found_optimal_solution(live_nodes):
    """
    Function that takes a list of Nodes and finds if the highest
    upper bound node is optimal. The highest upper bound node is optimal
    if there is no None value in it (thus the vector is complete).
    """
    candidate_node = _get_highest_upper_bound_node(live_nodes)

    if None not in candidate_node.branching_vector:
        return True
    else:
        return False


def _find_childs_branching_vector(branching_vector):
    """
    Function that takes a list that represent branching vector
    and returns the branching vectors of both his children.
    It will recieve a list that contains zero or more items
    that are (0 or 1) followed by one or more None values.
    This function will create two new lists that differ from the originla
    branching vector by the value of the first encountered None value.
    The left chlild will replace the first encountered
    None with 1, and the right child with 0.
    """
    index = branching_vector.index(None)
    left_branching_vector = branching_vector[:]
    left_branching_vector[index] = 1
    right_branching_vector = branching_vector[:]
    right_branching_vector[index] = 0
    return left_branching_vector, right_branching_vector
