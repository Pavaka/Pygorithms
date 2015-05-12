class Node:

    def __init__(self):
        value = 0
        weight = 0
        upper_bound = 0
        branching_vector = list()


def knapsack_problem_BnB(items, capacity):
    """

    """
    def _calculate_value_weight_of_node(node):
        sub_vercotr = [node.branching_vector[i] for i in node.branching_vector if node.branching_vector[i] != None]
        # for item in range(node.)

    def _calculate_upper_bound(node):
        pass



    number_of_items = len(items)

    root_node = Node()
    root_node.branching_vector = [None for _ in range(number_of_items)]

    root_node = _calculate_value_weight_of_node(root_node)


    root_node.upper_bound = _calculate_upper_bound(root_node)

    live_nodes = list()
    while True:

        if _check_for_optimal_node(live_nodes)[0] == True:
            optimal_node = _check_for_optimal_node[1]
            return optimal_node.value, optimal_node.branching_vector
        else:
            branching_node = _check_for_optimal_node[1]





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


items = [(3, 4), (2, 3), (4, 2), (4, 3)]
capacity = 6
answer = knapsack_problem_BnB(items, capacity)
