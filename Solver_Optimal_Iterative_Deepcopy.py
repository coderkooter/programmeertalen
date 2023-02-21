from knapsackclass import Knapsack
import copy


class Solver_Optimal_Iterative_Deepcopy():
    def __init__(self):
        self._solutions = {}
        self._solution = None

    def get_best_knapsack(self):
        return self._solution

    def solve(self, knapsack, items):
        self._solution = knapsack
        stack = copy.deepcopy(items)
        knapsack_copy = copy.deepcopy(knapsack)
        visited = []
        while len(visited) != len(items):
            cur_pos = len(items) - len(visited) - 1
            item = stack.pop(cur_pos)

            visited.append(item)
            while len(stack) != 0:
                knapsack_copy.add_item(item)
                item = stack.pop()
            if knapsack_copy.get_points() > self._solution.get_points():
                self._solution = copy.deepcopy(knapsack_copy)
            stack = copy.deepcopy(items)
            item = visited[len(visited) - 1]
            knapsack_copy.reset()
            while len(stack) != 0:
                item = stack.pop()
                knapsack_copy.add_item(item)
            if knapsack_copy.get_points() > self._solution.get_points():
                self._solution = copy.deepcopy(knapsack_copy)
            stack = copy.deepcopy(items)
            knapsack_copy.reset()
