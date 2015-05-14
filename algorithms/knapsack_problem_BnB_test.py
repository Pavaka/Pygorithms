import unittest
import knapsack_problem_BnB
print(knapsack_problem_BnB)


class TestKnapsackBnB(unittest.TestCase):

    def test_optimal_value_exmp_1(self):

        items = [(45, 3), (30, 5), (45, 9), (10, 5)]
        capacity = 16
        optimal_value = knapsack_problem_BnB.\
            knapsack_problem_BnB(items, capacity)[0]
        self.assertEqual(optimal_value, 90)

    def test_optimal_solution_exmp_1(self):
        items = [(45, 3), (30, 5), (45, 9), (10, 5)]
        capacity = 16
        optimal_solution = knapsack_problem_BnB.\
            knapsack_problem_BnB(items, capacity)[1]
        self.assertEqual(optimal_solution, [1, 0, 1, 0])

    def test_optimal_value_exmp_2(self):

        items = [(45, 3), (30, 5), (45, 9), (10, 5)]
        capacity = 1
        optimal_value = knapsack_problem_BnB.\
            knapsack_problem_BnB(items, capacity)[0]
        self.assertEqual(optimal_value, 0)

    def test_optimal_solution_exmp_2(self):
        items = [(45, 3), (30, 5), (45, 9), (10, 5)]
        capacity = 1
        optimal_solution = knapsack_problem_BnB.\
            knapsack_problem_BnB(items, capacity)[1]
        self.assertEqual(optimal_solution, [0, 0, 0, 0])

    def test_optimal_value_exmp_3(self):
        items = [(12, 4), (10, 6), (8, 5), (11, 7), (14, 3), (7, 1), (9, 6)]
        capacity = 18
        optimal_value = knapsack_problem_BnB.\
            knapsack_problem_BnB(items, capacity)[0]
        self.assertEqual(optimal_value, 44)

    def test_optimal_solution_exmp_3(self):
        items = [(12, 4), (10, 6), (8, 5), (11, 7), (14, 3), (7, 1), (9, 6)]
        capacity = 18
        optimal_value = knapsack_problem_BnB.\
            knapsack_problem_BnB(items, capacity)[1]
        self.assertEqual(optimal_value, [1, 1, 1, 0, 0, 1, 0])

    def test_negative_capacity_error(self):
        items = [(45, 3), (30, 5), (45, 9), (10, 5)]
        capacity = -5
        with self.assertRaises(knapsack_problem_BnB.NegativeCapacityError):
            knapsack_problem_BnB.knapsack_problem_BnB(items, capacity)

    def test_negative_value_item_error(self):
        items = [(45, 3), (30, 5), (-45, 9), (10, 5)]
        capacity = 1
        with self.assertRaises(knapsack_problem_BnB.NegativeValueItemError):
            knapsack_problem_BnB.knapsack_problem_BnB(items, capacity)

    def test_negative_weight_item_error(self):
        items = [(45, 3), (30, 5), (45, 9), (10, -5)]
        capacity = 1
        with self.assertRaises(knapsack_problem_BnB.NegativeWeightItemError):
            knapsack_problem_BnB.knapsack_problem_BnB(items, capacity)

    def test_invalid_items_exmp_1(self):
        items = "Items"
        capacity = 1
        with self.assertRaises(TypeError):
            knapsack_problem_BnB.knapsack_problem_BnB(items, capacity)

    def test_invalid_items_exmp_2(self):
        items = [(45, 3), 3, (45, 9), (10, 5)]
        capacity = 1
        with self.assertRaises(TypeError):
            knapsack_problem_BnB.knapsack_problem_BnB(items, capacity)

    def test_invalid_capacity(self):
        items = [(45, 3), 3, (45, 9), (10, 5)]
        capacity = "This is not capacity"
        with self.assertRaises(TypeError):
            knapsack_problem_BnB.knapsack_problem_BnB(items, capacity)


class TestCalculateValueWeightOfNode(unittest.TestCase):

    def setUp(self):
        self.items = [(9, 5), (3, 2), (5, 5), (3, 4)]
        self.capacity = 10
        self.problem_def = (self.items, self.capacity)

    def test_val_weight_of_node_1(self):
        node = knapsack_problem_BnB.Node()
        node.branching_vector = [None, None, None, None]
        val_weight = knapsack_problem_BnB._calculate_value_weight_of_node(
            self.problem_def, node)
        self.assertEqual(val_weight[0], 0)
        self.assertEqual(val_weight[1], 0)

    def test_val_weight_of_node_2(self):
        node = knapsack_problem_BnB.Node()
        node.branching_vector = [1, None, None, None]
        val_weight = knapsack_problem_BnB._calculate_value_weight_of_node(
            self.problem_def, node)
        self.assertEqual(val_weight[0], 9)
        self.assertEqual(val_weight[1], 5)

    def test_val_weight_of_node_3(self):
        node = knapsack_problem_BnB.Node()
        node.branching_vector = [1, 1, 0, None]
        val_weight = knapsack_problem_BnB._calculate_value_weight_of_node(
            self.problem_def, node)
        self.assertEqual(val_weight[0], 12)
        self.assertEqual(val_weight[1], 7)


class TestCalculateUpperBound(unittest.TestCase):

    def setUp(self):
        self.items = [(45, 3), (30, 5), (45, 9), (10, 5)]
        self.capacity = 16
        self.problem_def = (self.items, self.capacity)

    def test_upper_bound_of_node_1(self):
        node = knapsack_problem_BnB.Node()
        node.branching_vector = [1, 0, None, None]
        node.value = 45
        node.weight = 3
        upper_bound = knapsack_problem_BnB._calculate_upper_bound(
            self.problem_def, node)
        self.assertEqual(upper_bound, 98)

    def test_upper_bound_of_node_2(self):
        node = knapsack_problem_BnB.Node()
        node.branching_vector = [None, None, None, None]
        node.value = 0
        node.weight = 0
        upper_bound = knapsack_problem_BnB._calculate_upper_bound(
            self.problem_def, node)
        self.assertEqual(upper_bound, 115)

    def test_upper_bound_of_node_3(self):
        node = knapsack_problem_BnB.Node()
        node.branching_vector = [1, 1, 1, None]
        node.value = 120
        node.weight = 17
        upper_bound = knapsack_problem_BnB._calculate_upper_bound(
            self.problem_def, node)
        self.assertEqual(upper_bound, knapsack_problem_BnB.
                         no_upper_bound_value)

    def test_upper_bound_no_solution(self):
        self.capacity = 0
        self.problem_def = (self.items, self.capacity)
        node = knapsack_problem_BnB.Node()
        node.branching_vector = [None, None, None, None]
        upper_bound = knapsack_problem_BnB._calculate_upper_bound(
            self.problem_def, node)
        self.assertEqual(upper_bound, 0)


class TestGetHighestUpperBound(unittest.TestCase):

    def test_highest_upper_bound(self):

        node1 = knapsack_problem_BnB.Node()
        node2 = knapsack_problem_BnB.Node()
        node3 = knapsack_problem_BnB.Node()
        node1.upper_bound = 20
        node2.upper_bound = 30
        node3.upper_bound = 10
        live_nodes = [node1, node2, node3]

        highest_upper_bound_node = knapsack_problem_BnB.\
            _get_highest_upper_bound_node(live_nodes)

        self.assertEqual(highest_upper_bound_node, node2)


class TestFoundOptimalSolutionNode(unittest.TestCase):

    def setUp(self):
        self.items = [(45, 3), (30, 5), (45, 9), (10, 5)]
        self.capacity = 16
        self.problem_def = (self.items, self.capacity)

        self.node1 = knapsack_problem_BnB.Node()
        self.node1.branching_vector = [1, 0, None, None]
        self.node1.upper_bound = 100

        self.node2 = knapsack_problem_BnB.Node()
        self.node2.branching_vector = [0, 1, 1, None]
        self.node2.upper_bound = 60

        self.node3 = knapsack_problem_BnB.Node()
        self.node3.branching_vector = [1, 0, 1, 1]
        self.node3.upper_bound = 70

    def test_found_optimal_node_true(self):

        node4 = knapsack_problem_BnB.Node()
        node4.branching_vector = [1, 0, 1, 1]
        node4.upper_bound = 110
        live_nodes = [self.node1, self.node2, self.node3, node4]
        self.assertTrue(knapsack_problem_BnB.
                        _found_optimal_solution(live_nodes))

    def test_found_optimal_node_false(self):
        live_nodes = [self.node1, self.node2, self.node3]
        self.assertFalse(knapsack_problem_BnB.
                         _found_optimal_solution(live_nodes))


class TestFindBranchingVector(unittest.TestCase):

    def test_left_right_branching_vectors(self):
        branching_vector = [1, 0, 1, None]
        result = knapsack_problem_BnB.\
            _find_childs_branching_vector(branching_vector)
        left_vector = result[0]
        right_vector = result[1]
        self.assertEqual(left_vector, [1, 0, 1, 1])
        self.assertEqual(right_vector, [1, 0, 1, 0])


if __name__ == '__main__':
    unittest.main()
