from knapsackclass import Knapsack
import copy


class Solver_Optimal_Recursive():
    def __init__(self):
        self._solutions = {}
        self._solution = None

    def get_best_knapsack(self):
        return self._solution

    def solve(self, knapsack, items):
        self._solution = copy.deepcopy(knapsack)
        for i in range(len(items)):
            items.append(items.pop(i))
            self.solve_rec(knapsack, items.copy())
            knapsack.reset()

    def solve_rec(self, knapsack, items):
        if not items:
            if self.get_best_knapsack().get_points() < knapsack.get_points():
                self._solution = copy.deepcopy(knapsack)
            return

        item = items.pop()
        if knapsack.add_item(item):
            self.solve_rec(knapsack, items)

        knapsack.remove_item(item)
        self.solve_rec(knapsack, items)
