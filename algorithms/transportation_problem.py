balancing_flags = ("balanced", "additional row", "additional column")


class transportationCell:

    def __init__(self, cost):
        self.cost = cost
        self.amount = None


def transportation_problem(costs=None, vector_a=None, vector_b=None):
    # check_input(costs, vector_a, vector_b)
    table_rows = len(vector_a)
    table_columns = len(vector_b)
    costs = convert_costs_to_two_dimensional(costs, table_rows, table_columns)
    transportation_table, balancing_flag = create_transportation_table(costs, vector_a, vector_b)


def convert_costs_to_two_dimensional(costs, table_rows, table_columns):
    costs_two_dimensional = []
    for i in range(table_rows):
        row_cost = []
        for j in range(table_columns):
            row_cost.append(costs[j + i*table_columns])
        costs_two_dimensional.append(row_cost)
    return costs_two_dimensional


def create_transportation_table(costs, vector_a, vector_b):
    sum_vecotr_a = 0
    sum_vecotr_b = 0
    for value in vector_a:
        sum_vecotr_a += value
    for value in vector_b:
        sum_vecotr_b += value

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
            row_values.append(transportationCell(costs[i][j]))
        transportation_table.append(row_values)

    if balancing_flag == balancing_flags[0]:
        return transportation_table, balancing_flag, vector_a, vector_b
    elif balancing_flag == balancing_flags[1]:
        new_row = [transportationCell(0)] * table_columns
        transportation_table.append(new_row)
    elif balancing_flag == balancing_flags[2]:
        for row in range(table_rows):
            transportation_table[row].append(transportationCell(0))

    return transportation_table, balancing_flag, vector_a, vector_b