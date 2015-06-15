balancing_flags = ("balanced", "additional row", "additional column")
no_next_None_cell = "No next None cell", "No next None cell"


class TransportationCell:

    def __init__(self, cost):
        self.cost = cost
        self.amount = None


def transportation_problem(costs=None, vector_a=None, vector_b=None):
    # check_input(costs, vector_a, vector_b)
    table_rows = len(vector_a)
    table_columns = len(vector_b)
    costs = convert_costs_to_two_dimensional(costs, table_rows, table_columns)
    empty_transportation_table, balancing_flag, vector_a, vector_b\
        = create_transportation_table(costs, vector_a, vector_b)
    transportation_table = find_first_transportation_table(
        empty_transportation_table, vector_a, vector_b)

    transportation_table, found_optimal_solution = find_optimal_solution(transportation_table)

    while not found_optimal_solution:
        transportation_table, found_optimal_solution = find_optimal_solution(transportation_table)

    # return otgovora po nqkakuv nachin




def convert_costs_to_two_dimensional(costs, table_rows, table_columns):
    costs_two_dimensional = []
    for i in range(table_rows):
        row_cost = []
        for j in range(table_columns):
            row_cost.append(costs[j + i*table_columns])
        costs_two_dimensional.append(row_cost)
    return costs_two_dimensional


def create_transportation_table(costs, vector_a, vector_b):

    sum_vecotr_a = sum(vector_a)
    sum_vecotr_b = sum(vector_b)
    difference_between_vectors_sums = abs(sum_vecotr_a - sum_vecotr_b)

    if sum_vecotr_a > sum_vecotr_b:
        balancing_flag = balancing_flags[2]
        vector_b.append(difference_between_vectors_sums)
    elif sum_vecotr_a < sum_vecotr_b:
        balancing_flag = balancing_flags[1]
        vector_a.append(difference_between_vectors_sums)
    else:
        balancing_flag = balancing_flags[0]

    table_rows = len(costs)
    table_columns = len(costs[0])

    transportation_table = []
    for i in range(table_rows):
        row_values = []
        for j in range(table_columns):
            row_values.append(TransportationCell(costs[i][j]))
        transportation_table.append(row_values)

    if balancing_flag == balancing_flags[0]:
        return transportation_table, balancing_flag, vector_a, vector_b
    elif balancing_flag == balancing_flags[1]:
        new_row = [TransportationCell(0)] * table_columns
        transportation_table.append(new_row)
    elif balancing_flag == balancing_flags[2]:
        for row in range(table_rows):
            transportation_table[row].append(TransportationCell(0))

    return transportation_table, balancing_flag, vector_a, vector_b


def find_first_transportation_table(transportation_table, vector_a, vector_b):
    i = 0
    j = 0
    last_transportation_table_cell = transportation_table[-1][-1]
    while True:
        Ai = vector_a[i]
        Bi = vector_b[j]
        theta = min(Ai, Bi)
        transportation_table[i][j].amount = theta
        vector_a[i] -= theta
        vector_b[j] -= theta

        if transportation_table[i][j] is last_transportation_table_cell:
            return transportation_table

        if vector_a[i] == 0:
            i += 1
        elif vector_b[j] == 0:
            j += 1


def find_optimal_solution(transportation_table):
    i = 0
    j = 0

    while True:
        i, j = find_next_not_None_cell(transportation_table, i, j)
        if (i, j) == no_next_None_cell:
            return transportation_table, True
        elif i < len(transportation_table) - 1:
            i += 1
        elif j < len(transportation_table[0]) - 1:
            j += 1

        table_graph_cells = find_cells_graph(transportation_table, i, j)
        is_positive_cell = calculate_cell_value(table_graph_cells)
        if not is_positive_cell:
            new_transportation_table = calculate_new_TT()
            return new_transportation_table, False


def find_next_not_None_cell(transportation_table, i, j):
    table_rows = len(transportation_table)
    table_columns = len(transportation_table[0])
    while True:
        if transportation_table[i][j].amount is not None:
            if j < table_columns - 1:
                j += 1
                continue
            elif j == table_columns - 1 and i < table_rows - 1:
                j = 0
                i += 1
                continue
            else:
                return no_next_None_cell
        else:
            return i, j



def find_cells_graph(transportation_table, i , j):
    graph_cells_coords = []
    graph_cells_coords.append((i, j))

    return []

def calculate_cell_value(table_graph_cells):
    return bool

def calculate_new_TT(transportation_table):
    return