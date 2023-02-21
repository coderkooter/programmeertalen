import random
from knapsackclass import Knapsack
import copy


class Solver_Random():
    def __init__(self, n):
        self._iterations = n
        self._solution = []
        self._best_points = 0
        self._best_solution = None

    def get_best_knapsack(self):
        self._best_solution.reset()
        for item in self._solution:
            self._best_solution.add_item(item)
        return self._best_solution

    def solve(self, knapsack, items):
        self._best_solution = knapsack
        for i in range(self._iterations):
            visited = []
            no_add = 0
            while len(items) != 0 and no_add < 300:
                item = items.pop(random.randint(0, len(items) - 1))
                if knapsack.add_item(item) == False:
                    visited.append(item)
                    no_add += 1

            best_items = []
            for item_best in knapsack.get_items():
                best_items.append(item_best)
            if self._best_points < knapsack.get_points():
                self._solution = best_items
                self._best_points = knapsack.get_points()
                knapsack.reset()

            for item in best_items:
                items.append(item)
            for item in visited:
                items.append(item)
