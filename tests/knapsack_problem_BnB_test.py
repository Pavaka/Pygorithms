import unittest
import sys
import os
path = os.path.abspath("../algorithms")
sys.path.append(path)
import knapsack_problem_BnB as KPBnB


class TestKnapsackBnB(unittest.TestCase):

    def test_optimal_value_exmp_1(self):

        items = [(45, 3), (30, 5), (45, 9), (10, 5)]
        capacity = 16
        optimal_value = KPBnB.\
            knapsack_problem_BnB(items, capacity)[0]
        self.assertEqual(optimal_value, 90)

    def test_optimal_solution_exmp_1(self):
        items = [(45, 3), (30, 5), (45, 9), (10, 5)]
        capacity = 16
        optimal_solution = KPBnB.\
            knapsack_problem_BnB(items, capacity)[1]
        self.assertEqual(optimal_solution, [1, 0, 1, 0])

    def test_optimal_value_exmp_2(self):

        items = [(45, 3), (30, 5), (45, 9), (10, 5)]
        capacity = 1
        optimal_value = KPBnB.\
            knapsack_problem_BnB(items, capacity)[0]
        self.assertEqual(optimal_value, 0)

    def test_optimal_solution_exmp_2(self):
        items = [(45, 3), (30, 5), (45, 9), (10, 5)]
        capacity = 1
        optimal_solution = KPBnB.\
            knapsack_problem_BnB(items, capacity)[1]
        self.assertEqual(optimal_solution, [0, 0, 0, 0])

    def test_optimal_value_exmp_3(self):
        items = [(12, 4), (10, 6), (8, 5), (11, 7), (14, 3), (7, 1), (9, 6)]
        capacity = 18
        optimal_value = KPBnB.\
            knapsack_problem_BnB(items, capacity)[0]
        self.assertEqual(optimal_value, 44)

    def test_optimal_solution_exmp_3(self):
        items = [(12, 4), (10, 6), (8, 5), (11, 7), (14, 3), (7, 1), (9, 6)]
        capacity = 18
        optimal_value = KPBnB.\
            knapsack_problem_BnB(items, capacity)[1]
        self.assertEqual(optimal_value, [1, 1, 1, 0, 0, 1, 0])

    def test_optimal_value_exmp_4(self):
        items = []
        capacity = 18
        optimal_value = KPBnB.\
            knapsack_problem_BnB(items, capacity)[0]
        self.assertEqual(optimal_value, 0)

    def test_optimal_solution_exmp_4(self):
        items = []
        capacity = 18
        optimal_value = KPBnB.\
            knapsack_problem_BnB(items, capacity)[1]
        self.assertEqual(optimal_value, [])


class TestCalculateValueWeightOfNode(unittest.TestCase):

    def setUp(self):
        self.items = [(9, 5), (3, 2), (5, 5), (3, 4)]
        self.capacity = 10
        self.problem_def = (self.items, self.capacity)

    def test_val_weight_of_node_1(self):
        node = KPBnB.Node()
        node.branching_vector = [None, None, None, None]
        val_weight = KPBnB._calculate_value_weight_of_node(
            self.problem_def, node)
        self.assertEqual(val_weight[0], 0)
        self.assertEqual(val_weight[1], 0)

    def test_val_weight_of_node_2(self):
        node = KPBnB.Node()
        node.branching_vector = [1, None, None, None]
        val_weight = KPBnB._calculate_value_weight_of_node(
            self.problem_def, node)
        self.assertEqual(val_weight[0], 9)
        self.assertEqual(val_weight[1], 5)

    def test_val_weight_of_node_3(self):
        node = KPBnB.Node()
        node.branching_vector = [1, 1, 0, None]
        val_weight = KPBnB._calculate_value_weight_of_node(
            self.problem_def, node)
        self.assertEqual(val_weight[0], 12)
        self.assertEqual(val_weight[1], 7)


class TestCalculateUpperBound(unittest.TestCase):

    def setUp(self):
        self.items = [(45, 3), (30, 5), (45, 9), (10, 5)]
        self.capacity = 16
        self.problem_def = (self.items, self.capacity)

    def test_upper_bound_of_node_1(self):
        node = KPBnB.Node()
        node.branching_vector = [1, 0, None, None]
        node.value = 45
        node.weight = 3
        upper_bound = KPBnB._calculate_upper_bound(
            self.problem_def, node)
        self.assertEqual(upper_bound, 98)

    def test_upper_bound_of_node_2(self):
        node = KPBnB.Node()
        node.branching_vector = [None, None, None, None]
        node.value = 0
        node.weight = 0
        upper_bound = KPBnB._calculate_upper_bound(
            self.problem_def, node)
        self.assertEqual(upper_bound, 115)

    def test_upper_bound_of_node_3(self):
        node = KPBnB.Node()
        node.branching_vector = [1, 1, 1, None]
        node.value = 120
        node.weight = 17
        upper_bound = KPBnB._calculate_upper_bound(
            self.problem_def, node)
        self.assertEqual(upper_bound, KPBnB.
                         no_upper_bound_value)

    def test_upper_bound_no_solution(self):
        self.capacity = 0
        self.problem_def = (self.items, self.capacity)
        node = KPBnB.Node()
        node.branching_vector = [None, None, None, None]
        upper_bound = KPBnB._calculate_upper_bound(
            self.problem_def, node)
        self.assertEqual(upper_bound, 0)


class TestGetHighestUpperBound(unittest.TestCase):

    def test_highest_upper_bound(self):

        node1 = KPBnB.Node()
        node2 = KPBnB.Node()
        node3 = KPBnB.Node()
        node1.upper_bound = 20
        node2.upper_bound = 30
        node3.upper_bound = 10
        live_nodes = [node1, node2, node3]

        highest_upper_bound_node = KPBnB.\
            _get_highest_upper_bound_node(live_nodes)

        self.assertEqual(highest_upper_bound_node, node2)


class TestFoundOptimalSolutionNode(unittest.TestCase):

    def setUp(self):
        self.items = [(45, 3), (30, 5), (45, 9), (10, 5)]
        self.capacity = 16
        self.problem_def = (self.items, self.capacity)

        self.node1 = KPBnB.Node()
        self.node1.branching_vector = [1, 0, None, None]
        self.node1.upper_bound = 100

        self.node2 = KPBnB.Node()
        self.node2.branching_vector = [0, 1, 1, None]
        self.node2.upper_bound = 60

        self.node3 = KPBnB.Node()
        self.node3.branching_vector = [1, 0, 1, 1]
        self.node3.upper_bound = 70

    def test_found_optimal_node_true(self):

        node4 = KPBnB.Node()
        node4.branching_vector = [1, 0, 1, 1]
        node4.upper_bound = 110
        live_nodes = [self.node1, self.node2, self.node3, node4]
        self.assertTrue(KPBnB.
                        _found_optimal_solution(live_nodes))

    def test_found_optimal_node_false(self):
        live_nodes = [self.node1, self.node2, self.node3]
        self.assertFalse(KPBnB.
                         _found_optimal_solution(live_nodes))


class TestFindBranchingVector(unittest.TestCase):

    def test_left_right_branching_vectors(self):
        branching_vector = [1, 0, 1, None]
        result = KPBnB.\
            _find_childs_branching_vector(branching_vector)
        left_vector = result[0]
        right_vector = result[1]
        self.assertEqual(left_vector, [1, 0, 1, 1])
        self.assertEqual(right_vector, [1, 0, 1, 0])


if __name__ == '__main__':
    unittest.main()
