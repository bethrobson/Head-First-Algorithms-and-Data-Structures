
def greedy_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    sorted_items = sorted(items, key=lambda x: x["value"] / x["weight"], reverse=True)

    total_value = 0
    total_weight = 0
    selected_items = []

    for item in sorted_items:
        # print(f'value/weight for {item}: {item["value"]/item["weight"]}')
        if total_weight + item["weight"] <= capacity:
            selected_items.append(item["name"])
            total_weight += item["weight"]
            total_value += item["value"]
    
    return selected_items, total_weight, total_value

# Define the items
items = [
    {"name": "Gold coins", "weight": 10, "value": 500},
    {"name": "Silver goblets", "weight": 20, "value": 800},
    {"name": "Ancient scrolls", "weight": 5, "value": 300},
    {"name": "Jeweled crown", "weight": 25, "value": 1200},
    {"name": "Diamond necklaces", "weight": 15, "value": 1000}
]

# Max weight the person can carry
capacity = 50

# Run the greedy knapsack
chosen_items, weight, value = greedy_knapsack(items, capacity)

print("Items chosen:", chosen_items)
print("Total weight:", weight)
print("Total value:", value)


