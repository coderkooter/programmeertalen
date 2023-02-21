import random
from knapsackclass import Knapsack
import copy


class Solver_Random_Improved():
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

    def random_solution(self, knapsack, items):
        self._best_solution = knapsack
        for i in range(1000):
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

    def solve(self, knapsack, items):
        self._best_solution = knapsack
        # visited = []
        # while len(items) != 0:
        #     item = items.pop(random.randint(0, len(items) - 1))
        #     if knapsack.add_item(item) == False:
        #         visited.append(item)

        # for item in visited:
        #     items.append(item)
        self.random_solution(knapsack, items)
        knapsack = self.get_best_knapsack()

        temperature = 10

        for i in range(self._iterations):
            if(len(items) == 0):
                break
            score_before = knapsack.get_points()
            item_one = items.pop(random.randint(0, len(items) - 1))
            if knapsack.add_item(item_one):
                continue
            item_two = knapsack.remove_item_at_pos(
                random.randint(0, len(knapsack.get_items()) - 1))
            if knapsack.add_item(item_one):
                score_after = knapsack.get_points()
                chance = random.randint(0, 10)
                if score_before > score_after or chance > temperature:
                    items.append(item_one)
                    knapsack.add_item(item_two)
                else:
                    items.append(item_two)
            else:
                items.append(item_one)
                knapsack.add_item(item_two)

        self._solution = knapsack.get_items()
