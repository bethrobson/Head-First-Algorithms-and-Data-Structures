
import itertools

# Define the items
items = [
    {"name": "Gold coins", "weight": 10, "value": 500},
    {"name": "Silver goblets", "weight": 20, "value": 800},
    {"name": "Ancient scrolls", "weight": 5, "value": 300},
    {"name": "Jeweled crowns", "weight": 25, "value": 1200},
    {"name": "Diamond necklaces", "weight": 15, "value": 1000}
]

# Knapsack capacity
capacity = 50

# Best combination tracking
best_combo = None
best_value = 0
best_weight = 0
num_combos = 0

# Generate all possible combinations (any number of items)
for r in range(1, len(items) + 1):
    for combination in itertools.combinations(items, r):
        num_combos += 1
        # print(f"#{num_combos} Combination: {combination}")
        total_weight = sum(item['weight'] for item in combination)
        total_value = sum(item['value'] for item in combination)
        
        # Check if combination fits in the knapsack and if it's better than the best so far
        if total_weight <= capacity and total_value > best_value:
            best_combo = combination
            best_value = total_value
            best_weight = total_weight

# Output the best result
print("Total number of combinations:", num_combos)
print("Best combination of items:")
for item in best_combo:
    print(f"- {item['name']} (Weight: {item['weight']}, Value: {item['value']})")
print(f"Total weight: {best_weight}")
print(f"Total value: {best_value}")


for n in [10, 20, 50]:
    print(f"n = {n}, (2 ** n) - 1 = {(2 ** n) - 1}")



