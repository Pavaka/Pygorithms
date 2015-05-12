class Node:

    def __init__(self):
        self.value = 0
        self.weight = 0
        self.upper_bound = 0
        self.branching_vector = list()


def knapsack_problem_BnB(items, capacity):
    """

    """

    problem_definition = (items, capacity)
    number_of_items = len(items)

    root_node = Node()
    root_node.branching_vector = [None for _ in range(number_of_items)]

    # val_weight = _calculate_value_weight_of_node(problem_definition, root_node)
    # root_node.value = val_weight[0]
    # root_node.weight = val_weight[1]

    root_node.upper_bound = _calculate_upper_bound(problem_definition,
                                                   root_node)
    live_nodes = [root_node]

    while True:

        highest_upper_bound_node = _get_highest_upper_bound_node(live_nodes)

        if _found_optimal_solution:
            return highest_upper_bound_node.value, highest_upper_bound_node.branching_vector
        






        if _check_for_optimal_node(live_nodes)[0] == True:
            optimal_node = _check_for_optimal_node[1]
            return optimal_node.value, optimal_node.branching_vector
        else:
            branching_node = _check_for_optimal_node[1]


def _calculate_value_weight_of_node(problem_def, node):
    items = problem_def[0]
    # capacity = problem_def[1]
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
    items = problem_def[0]
    capacity = problem_def[1]
    upper_bound = node.value
    remaining_capacity = capacity - node.weight
    if remaining_capacity < 0:
        return -100

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


def _check_for_optimal_node(live_nodes):
    candidate_node = _get_highest_upper_bound_node(live_nodes)

    if None not in candidate_node.branching_vector:
        return True, candidate_node
    else:
        return False, candidate_node


def _get_highest_upper_bound_node(live_nodes):
    highest_upper_bound_node = live_nodes[0]
    for node in live_nodes:
        if node.upper_bound > highest_upper_bound_node.upper_bound:
            highest_upper_bound_node = node
    return highest_upper_bound_node


def _found_optimal_solution(live_nodes):
    candidate_node = _get_highest_upper_bound_node(live_nodes)

    if None not in candidate_node.branching_vector:
        return True
    else:
        return False

def _find_childs_branching_vector(branching_vector):
    index = branching_vector.index[None]

# items = [(45, 3), (30, 5), (45, 9), (10, 5)]
# capacity = 16
# # # # answer = knapsack_problem_BnB(items, capacity)
# # # prb_df=(items, capacity)
# # # note = Node()
# # # note.branching_vector = [1, None, None, None]
# # # _calculate_value_weight_of_node(prb_df, note)
# knapsack_problem_BnB(items, capacity)
