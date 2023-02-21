from item import Item
from knapsackclass import Knapsack


def load_knapsack(file_name):
    items = []
    sack = 0
    with open(file_name) as file:
        next(file)
        for line in file:
            current_item = line.strip().split(", ")
            if current_item[0] == "knapsack":
                sack = Knapsack(
                    current_item[0], int(current_item[1]), int(current_item[2]), int(current_item[3]))
            else:
                items.append(Item(
                    current_item[0], int(current_item[1]), int(current_item[2]), int(current_item[3])))

    return sack, items
