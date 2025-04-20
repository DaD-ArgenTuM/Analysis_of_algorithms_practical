# Item class to store value and weight
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(items, capacity):
    # Step 1: Sort items by value/weight ratio in descending order
    items.sort(key=lambda item: item.value / item.weight, reverse=True)

    total_value = 0.0  # Total value in knapsack
    for item in items:
        if capacity >= item.weight:
            # If the item can be taken fully
            capacity -= item.weight
            total_value += item.value
        else:
            # Take the fraction of the remaining capacity
            total_value += item.value * (capacity / item.weight)
            break  # Knapsack is full

    return total_value

# Example usage
items = [
    Item(60, 10),  # value, weight
    Item(100, 20),
    Item(120, 30)
]
capacity = 50

max_value = fractional_knapsack(items, capacity)
print("Maximum value in knapsack:", max_value)
