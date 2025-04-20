# Fractional Knapsack Problem using Greedy Method

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Value-to-weight ratio

def fractional_knapsack(capacity, items):
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0  # Total value of items in the knapsack
    for item in items:
        if capacity >= item.weight:
            # If the item can fit entirely, take it
            capacity -= item.weight
            total_value += item.value
        else:
            # If the item can't fit entirely, take the fraction that fits
            total_value += item.ratio * capacity
            break

    return total_value

# Example usage
if __name__ == "__main__":
    # List of items (value, weight)
    items = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30)
    ]
    capacity = 50  # Knapsack capacity

    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value in the knapsack: {max_value}")