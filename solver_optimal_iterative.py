from knapsackclass import Knapsack


class Solver_Optimal_Iterative():
    def __init__(self):
        self._solutions = {}
        self._solution = None
        self._best_solution = None
        self._current_best = 0

    def get_best_knapsack(self):
        self._best_solution.reset()
        for item in self._solution:
            self._best_solution.add_item(item)
        return self._best_solution

    def solve(self, knapsack, items):
        self._best_solution = knapsack
        self._solution = []
        stack = items
        visited = []
        while len(visited) != len(items):
            # print(f"{stack} \n")
            cur_pos = len(items) - len(visited) - 1
            item = stack[cur_pos]
            item_len = len(items)
            visited.append(item)
            added = 0
            while added != item_len:
                knapsack.add_item(item)
                item = stack[item_len - added - 1]
                added += 1
            if knapsack.get_points() > self._current_best:
                best_items = []
                for item_best in knapsack.get_items():
                    best_items.append(item_best)
                self._solution = best_items
                self._current_best = knapsack.get_points()
            knapsack.reset()
            added = 0
            while added != item_len:
                item = stack[item_len - added - 1]
                added += 1
            if knapsack.get_points() > self.get_best_knapsack().get_points():
                best_items = []
                for item_best in knapsack.get_items():
                    best_items.append(item_best)
                self._solution = best_items
            knapsack.reset()
