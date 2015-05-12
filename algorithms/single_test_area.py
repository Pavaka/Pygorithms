import unittest
import knapsack_problem_BnB

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
        self.assertTrue(knapsack_problem_BnB._found_optimal_solution(live_nodes))





if __name__ == '__main__':
    unittest.main()
