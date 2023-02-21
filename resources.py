from item import Item
import csv


class Resources:
    def __init__(self, name, points, weight, volume):
        self._current_points
        self._max_weight = weight
        self._max__volume = volume
        self._current_weight = 0
        self._current_volume = 0
        self._items = []

    def get_points(self):
        return self._current_points

    def get_weight(self):
        return self._max_weight

    def get_volume(self):
        return self._max__volume

    def get_current_weight(self):
        return self._current_weight

    def get_current_volume(self):
        return self._current_volume

    def get_items(self):
        return self._items

    def get_points(self):
        return self._current_points

    def reset(self):
        self._items = []
        self._current_volume = 0
        self._current_weight = 0
        self.current_points = 0

    def volume_left(self):
        return self.get_volume() - self.get_current_volume()

    def weight_left(self):
        return self.get_weight() - self.get_current_weight()

    def set_current_weight(self, weight):
        self._current_weight += weight

    def set_current_volume(self, volume):
        self._current_volume += volume

    def __add__(self, item):
        if (self.weight_left() < item.get_weight()) or (self.volume_left() < item.get_volume()) or (item.get_name() in self.get_item_names()):
            return False
        else:
            self._items.append(item)
            self.set_current_weight(item.get_weight())
            self.set_current_volume(item.get_volume())
            self.add_points(item.get_points())
            return True

    def get_item_names(self):
        names = []
        for item in self.get_items():
            names.append(item.get_name())

        return names

    def __sub__(self, item):
        if item.get_name() in list(map(lambda item: item.get_name(), self._items)):
            self._items.remove(item)
            self.remove_points((item.get_points()))
            self.set_current_weight(-(item.get_weight()))
            self.set_current_volume(-(item.get_volume()))
        # else:
            # print(f"item not in sack: {item.get_name()}")
            # print(
            #     f"control: sack is: {list(map(lambda item:item.get_name(), self.get_items()))}")

    def is_valid(self):
        for item in self._items:
            self._current_volume += item.get_volume()
            self._current_weight += item.get_weight()
            if self._weight - self._current_weight < 0:
                return False
            if self._volume - self._current_volume < 0:
                return False

        return True

    def set_items(self, items):
        self._items = items

    def remove_points(self, points):
        self._points -= points

    def add_points(self, points):
        self._points += points

    def set_solution(self, solution):
        self._solution = solution

    def save(self, solution_file):
        with open(solution_file, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            writer.writerow(["name", "points", "weight", "volume"])
            writer.writerow([self.get_name(), self.get_points(),
                            self.get_weight(), self.get_volume()])
            for item in self._items:
                writer.writerow(
                    [item.get_name(), item.get_points(), item.get_weight(), item.get_volume()])

    def remove_item_at_pos(self, index):
        if (index <= len(self._items) - 1):
            item = self._items.pop(index)
            self.remove_points((item.get_points()))
            self.set_current_weight(-(item.get_weight()))
            self.set_current_volume(-(item.get_volume()))
            return item
        return False

    def __gt__(self, knapsack_comp):
        return self.get_points() > knapsack_comp.get_points()

    def __len__(self):
        return len(self.get_items())
