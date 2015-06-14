import unittest
import sys
import os
path = os.path.abspath("..")
sys.path.append(path)
from algorithms.transportation_problem import *

class TestTransportationProblem(unittest.TestCase):

    def test_cots_to_two_dimensional(self):
        costs = [i for i in range(1, 13)]
        table_rows = 3
        table_columns = 4
        answer_expected = [[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [9, 10, 11, 12]]
        answer_returned = convert_costs_to_two_dimensional(costs, table_rows, table_columns)
        self.assertEqual(answer_returned, answer_expected)


class TestCreationTransportationTable(unittest.TestCase):

    def setUp(self):
        self.costs = [[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12]]
        self.vector_a = [100, 130, 170]
        self.vector_b = [150, 120, 80, 50]



    def test_create_transportation_table_balancig_flag(self):

        balncing_flag = create_transportation_table(self.costs, self.vector_a, self.vector_b)[1]
        self.assertEqual(balncing_flag, balancing_flags[0])
        self.vector_a[1] += 10
        balncing_flag = create_transportation_table(self.costs, self.vector_a, self.vector_b)[1]
        self.assertEqual(balncing_flag, balancing_flags[2])
        self.vector_b[2] += 30
        balncing_flag = create_transportation_table(self.costs, self.vector_a, self.vector_b)[1]
        self.assertEqual(balncing_flag, balancing_flags[1])

    def test_create_transportation_table_vector_a(self):
        self.vector_a = [100, 130, 210]
        result = create_transportation_table(self.costs, self.vector_a, self.vector_b)
        result_vector_a, result_vector_b =result[2],result[3]
        self.assertEqual(result_vector_a, self.vector_a)
        self.assertEqual([150, 120, 80, 50, 40], result_vector_b)

    def test_create_transportation_table_vector_b(self):
        self.vector_b = [150, 120, 80, 100]
        result = create_transportation_table(self.costs, self.vector_a, self.vector_b)
        result_vector_a, result_vector_b =result[2],result[3]
        self.assertEqual(result_vector_b, self.vector_b)
        self.assertEqual([100, 130, 170, 50], result_vector_a)

    def test_transportation_table_balanced(self):
        transportation_table = create_transportation_table(self.costs, self.vector_a, self.vector_b)[0]
        table_rows = len(transportation_table)
        table_columns = len(transportation_table[0])
        for i in range(table_rows):
            for j in range(table_columns):
                self.assertEqual(transportation_table[i][j].cost, self.costs[i][j])

    def test_transportation_table_unbalanced_additional_row(self):
        self.vector_b = [150, 120, 80, 70]
        transportation_table = create_transportation_table(self.costs, self.vector_a, self.vector_b)[0]
        table_rows = len(transportation_table)
        table_columns = len(transportation_table[0])
        for i in range(table_rows - 1):
            for j in range(table_columns):
                self.assertEqual(transportation_table[i][j].cost, self.costs[i][j])

        for j in range(table_columns):
            self.assertEqual(transportation_table[-1][j].cost, 0)

    def test_transportation_table_unbalanced_additional_column(self):
        self.vector_a = [100, 130, 200]
        transportation_table = create_transportation_table(self.costs, self.vector_a, self.vector_b)[0]
        table_rows = len(transportation_table)
        table_columns = len(transportation_table[0])
        last_column_index = table_columns - 1
        for i in range(table_rows):
            for j in range(table_columns):
                if j != last_column_index:
                    self.assertEqual(transportation_table[i][j].cost, self.costs[i][j])
                elif j == last_column_index:
                    self.assertEqual(transportation_table[i][j].cost, 0)

if __name__ == '__main__':
    unittest.main()
