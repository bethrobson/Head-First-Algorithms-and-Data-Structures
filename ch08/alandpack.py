
def greedy_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    # items = sorted(items, key=lambda x: x["value"] / x["weight"], reverse=True)
    items = sorted(items, key=lambda x: x["value"], reverse=True)
    print(items)

    total_value = 0
    total_weight = 0
    selected_items = []

    for item in items:
        print(f'value/weight for {item}: {item["value"]/item["weight"]}')
        if total_weight + item["weight"] <= capacity:
            selected_items.append(item["name"])
            total_weight += item["weight"]
            total_value += item["value"]
    
    return selected_items, total_weight, total_value

# Define the items
items = [
    {"name": "Map", "weight": 6, "value": 30},
    {"name": "Compass", "weight": 5, "value": 20},
    {"name": "Flashlight", "weight": 4, "value": 20},
    {"name": "Snacks", "weight": 3, "value": 18},
    {"name": "Water Bottle", "weight": 3, "value": 14}
]

# Max weight the person can carry
capacity = 10

# Run the greedy knapsack
chosen_items, weight, value = greedy_knapsack(items, capacity)

print("Items chosen:", chosen_items)
print("Total weight:", weight)
print("Total value:", value)


