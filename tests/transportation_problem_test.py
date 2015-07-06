import unittest
import sys
import os
path = os.path.abspath("..")
sys.path.append(path)
from pygorithms.transportation_problem import *


class TestTransportationProblem(unittest.TestCase):

    def test_costs_to_two_dimensional(self):
        costs = [i for i in range(1, 13)]
        table_rows = 3
        table_columns = 4
        answer_expected = [[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [9, 10, 11, 12]]
        answer_returned = convert_costs_to_two_dimensional(
            costs, table_rows, table_columns)
        self.assertEqual(answer_returned, answer_expected)

    def test_incompitible_vector_sizes_exmp1(self):
        costs = [i for i in range(1, 13)]
        vector_a = [100, 130, 170]
        vector_b = [150, 120, 80, 50, 20]
        with self.assertRaises(VectorSizesError):
            transportation_problem(costs, vector_a, vector_b)

    def test_incompitible_vector_sizes_exmp2(self):
        costs = [i for i in range(1, 14)]
        vector_a = [100, 130, 170]
        vector_b = [150, 120, 80, 50]
        with self.assertRaises(VectorSizesError):
            transportation_problem(costs, vector_a, vector_b)


class TestCreationTransportationTable(unittest.TestCase):

    def setUp(self):
        self.costs = [[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12]]
        self.vector_a = [100, 130, 170]
        self.vector_b = [150, 120, 80, 50]

    def test_create_balanced_transportation_table_balancig_flag(self):

        balncing_flag = create_balanced_transportation_table(self.costs, self.vector_a,
                                                    self.vector_b)[1]
        self.assertEqual(balncing_flag, balancing_flags[0])
        self.vector_a[1] += 10
        balncing_flag = create_balanced_transportation_table(self.costs, self.vector_a,
                                                    self.vector_b)[1]
        self.assertEqual(balncing_flag, balancing_flags[2])
        self.vector_b[2] += 30
        balncing_flag = create_balanced_transportation_table(self.costs, self.vector_a,
                                                    self.vector_b)[1]
        self.assertEqual(balncing_flag, balancing_flags[1])

    def test_create_balanced_transportation_table_vector_a(self):
        self.vector_a = [100, 130, 210]
        result = create_balanced_transportation_table(self.costs, self.vector_a,
                                             self.vector_b)
        result_vector_a, result_vector_b = result[2], result[3]
        self.assertEqual(result_vector_a, self.vector_a)
        self.assertEqual([150, 120, 80, 50, 40], result_vector_b)

    def test_create_balanced_transportation_table_vector_b(self):
        self.vector_b = [150, 120, 80, 100]
        result = create_balanced_transportation_table(self.costs, self.vector_a,
                                             self.vector_b)
        result_vector_a, result_vector_b = result[2], result[3]
        self.assertEqual(result_vector_b, self.vector_b)
        self.assertEqual([100, 130, 170, 50], result_vector_a)

    def test_transportation_table_balanced(self):
        transportation_table = create_balanced_transportation_table(
            self.costs, self.vector_a, self.vector_b)[0]
        table_rows = len(transportation_table)
        table_columns = len(transportation_table[0])
        for i in range(table_rows):
            for j in range(table_columns):
                self.assertEqual(transportation_table[i][j].cost,
                                 self.costs[i][j])

    def test_transportation_table_unbalanced_additional_row(self):
        self.vector_b = [150, 120, 80, 70]
        transportation_table = create_balanced_transportation_table(
            self.costs, self.vector_a, self.vector_b)[0]
        table_rows = len(transportation_table)
        table_columns = len(transportation_table[0])
        for i in range(table_rows - 1):
            for j in range(table_columns):
                self.assertEqual(transportation_table[i][j].cost,
                                 self.costs[i][j])

        for j in range(table_columns):
            self.assertEqual(transportation_table[-1][j].cost, 0)

    def test_transportation_table_unbalanced_additional_column(self):
        self.vector_a = [100, 130, 200]
        transportation_table = create_balanced_transportation_table(
            self.costs, self.vector_a, self.vector_b)[0]
        table_rows = len(transportation_table)
        table_columns = len(transportation_table[0])
        last_column_index = table_columns - 1
        for i in range(table_rows):
            for j in range(table_columns):
                if j != last_column_index:
                    self.assertEqual(transportation_table[i][j].cost,
                                     self.costs[i][j])
                elif j == last_column_index:
                    self.assertEqual(transportation_table[i][j].cost, 0)


class TestFirstTrnspTableFinder(unittest.TestCase):

    def test_first_transportation_table_balanced(self):
        costs = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]]
        vector_a = [100, 130, 170]
        vector_b = [150, 120, 80, 50]
        new_table = create_balanced_transportation_table(costs, vector_a, vector_b)[0]
        first_transp_table = find_first_transportation_table_amounts(
            new_table, vector_a, vector_b)

        amounts = [[100, None, None, None],
                   [50, 80, None, None],
                   [None, 40, 80, 50]]

        for i in range(len(vector_a)):
            for j in range(len(vector_b)):
                self.assertEqual(
                    first_transp_table[i][j].amount, amounts[i][j])
                self.assertEqual(first_transp_table[i][j].cost, costs[i][j])

    def test_first_transportation_table_unbalanced(self):
        costs = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]]
        vector_a = [100, 130, 200]
        vector_b = [150, 120, 80, 50]

        amounts = [[100, None, None, None, None],
                   [50, 80, None, None, None],
                   [None, 40, 80, 50, 30]]

        new_table = create_balanced_transportation_table(costs, vector_a, vector_b)[0]
        first_transp_table = find_first_transportation_table_amounts(
            new_table, vector_a, vector_b)

        for i in range(len(vector_a)):
            for j in range(len(vector_b)):
                self.assertEqual(
                    first_transp_table[i][j].amount, amounts[i][j])

class TestSuppFunctions(unittest.TestCase):

    def setUp(self):
        self.costs = [[3, 5, 7, 11],
                      [1, 4, 6, 3],
                      [5, 8, 12, 7]]
        self.vector_a = [100, 130, 170]
        self.vector_b = [150, 120, 80, 50]
        self.transp_table_balancer = create_balanced_transportation_table(
            self.costs, self.vector_a, self.vector_b)
        self.transp_table = find_first_transportation_table_amounts(
            self.transp_table_balancer[0], self.transp_table_balancer[2],
                self.transp_table_balancer[3])

    def test_find_next_None_cell(self):
        next_None_cell = find_next_None_cell(self.transp_table, 0, 0)
        self.assertEqual(next_None_cell, (0, 1))
        next_None_cell = find_next_None_cell(self.transp_table, 1, 0)
        self.assertEqual(next_None_cell, (1, 2))

    def test_find_lefter_not_None_cell(self):
        cells = find_lefter_not_None_cells(self.transp_table, (1, 2), (1, 2))
        self.assertEqual(cells, [(1, 1), (1, 0)])

    def test_find_righter_not_None_cell(self):
        cells = find_righter_not_None_cells(self.transp_table, (1, 2), (1, 2))
        self.assertEqual(cells, [])
        cells = find_righter_not_None_cells(self.transp_table, (2, 0), (2, 0))
        self.assertEqual(cells, [(2, 1), (2, 2), (2, 3)])

    def test_upper_not_None_cells(self):
        cells = find_upper_not_None_cells(self.transp_table, (2, 0), (2, 0))
        self.assertEqual(cells, [(1, 0), (0, 0)])

    def test_downer_not_None_cells(self):
        cells = find_downer_not_None_cells(self.transp_table, (0, 2), (2, 0))
        self.assertEqual(cells, [(2, 2)])

    def test_all_reachable_not_None_cells(self):
        cells = find_all_reachable_not_None_cells(
            self.transp_table, (1, 2), direction_not_to_go[4], (1, 2))
        self.assertEqual(cells, [(1, 1), (1, 0), (2, 2)])

    def test_extend_path_for_reachable_not_None_cells(self):
        path = [(0, 1), (1, 1)]
        extensible_cells = find_all_reachable_not_None_cells(
            self.transp_table, path[-1], direction_not_to_go[2], (0, 1))
        all_new_paths = extend_path_for_each_reachable_not_None_cell(
            path, extensible_cells)
        all_new_paths_expected = [
                                [(0, 1), (1, 1), (1, 0)],
                                [(0, 1), (1, 1), (2, 1)]
                                ]
        self.assertEqual(all_new_paths, all_new_paths_expected)

    def test_find_table_graph_cells_exmp1(self):
        graph_path_cells = find_table_graph_cells(self.transp_table, 0, 1)
        self.assertEqual(graph_path_cells, [(0, 1), (0, 0), (1, 0), (1, 1)])

    def test_find_table_graph_cells_exmp2(self):
        for row in self.transp_table:
            for cell in row:
                cell.amount = 10
        None_indexes = (3, 5, 6, 7, 8, 10)
        counter = 0
        for row in self.transp_table:
            for cell in row:
                if counter in None_indexes:
                    cell.amount = None
                counter += 1

        # for row in self.transp_table:
        #     for cell in row:
        #         print(cell.amount)
        graph_path_cells = find_table_graph_cells(self.transp_table, 1, 3)
        self.assertEqual(graph_path_cells, [
            (1, 3), (1, 0), (0, 0), (0, 1), (2, 1), (2, 3)])

if __name__ == '__main__':
    unittest.main()
