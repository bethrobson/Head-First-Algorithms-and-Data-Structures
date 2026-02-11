# Dynamic programming knapsack solution

def knapsack_dp(items, max_weight):
    step = 5 #create table in 5 pound increments
    n = len(items)
    w = max_weight // step # number of capacity columns (0, 5, 10, ... 50)

    # creates a table of 6 rows (0-5 items) and 11 columns (0... 50 lbs)
    # initially, everything is 0
    dp = [[0] * (w + 1) for _ in range(n + 1)]

    # row i corresponds to items[i - 1]
    for i in range(1, n+1): # looping through items
        item = items[i - 1]
        # e.g. if weight is 10, weight units is 2
        weight_units = item["weight"] // step
        value = item["value"]

        # weight is capacity in units of 5 pounds
        for weight in range(w + 1): # looping through capacity
            # if the current capacity can hold the item
            if weight_units <= weight:
            # Take or don't take item?
                dp[i][weight] = max(
                              # don't take it;
                              # take previous row at this capacity
                              dp[i-1][weight], # don't take it
                              # take it
                              # the new item will fit (weight units <= weight)
                              # taking it reduces weight capacity by weight units
                              # taking it requires solving smaller knapsack problem
                              # dp[i-1][weight - weight_units] is previously solved 
                              #  subproblem
                              # best value achievable before this item, using the
                              #  remaining capacity, plus this item's value
                              dp[i-1][weight - weight_units] + value # take item
                )
            else:
                dp[i][weight] = dp[i-1][weight] # won't fit, copy previous row
    return dp

# Recover which items we took from the table
def recover_items(dp, items, max_weight):
    step = 5
    weight = max_weight // step
    i = len(items)
    chosen_items = []

    # Start at the bottom right corner (i.e. the best value)
    while i > 0 and weight > 0:
        # Did the value change when this item was introduced?
        # If yes, the item was taken (the value changed between rows)
        # If no, the item was not taken (the value stayed the same)
        if dp[i][weight] != dp[i-1][weight]:
            # the item was taken
            item = items[i - 1]  # record the item
            chosen_items.append(item["name"])
            # we took the item, so reduce capacity by its weight
            # this jumps us left in the table
            weight -= item["weight"] // step
            # now we ask: what was the best solution before this item was added
        i -= 1 # regardless of take or skip, we move to the previous item

    return chosen_items[::-1] 

# pretty print the table
def print_dp_table(dp, items, max_weight):
    step = 5
    w = max_weight // step

    header = ["Item \\ Wt"]
    for weight in range(w + 1):
        header.append(f"{weight * step:>4}")
    print(" | ".join(header))
    print("-" * (len(header) * 7))

    for i in range(len(dp)):
        if i == 0:
            row_label = "None"
        else:
            row_label = items[i - 1]["name"]
        row = [f"{row_label:<15}"]
        for weight in range(w + 1):
            row.append(f"{dp[i][weight]:>4}")
        print(" | ".join(row))

# Our items
items = [
    {"name": "Gold coins", "weight": 10, "value": 500},
    {"name": "Silver goblets", "weight": 20, "value": 800},
    {"name": "Ancient scrolls", "weight": 5, "value": 300},
    {"name": "Jeweled crown", "weight": 25, "value": 1200},
    {"name": "Diamond necklaces", "weight": 15, "value": 1000}
]

# Max weight the person can carry
capacity = 50

dp_table = knapsack_dp(items, capacity)
chosen_items = recover_items(dp_table, items, capacity)

print("---------------")
print_dp_table(dp_table, items, capacity)
print("\nMaximum value:", dp_table[len(items)][capacity // 5])
print("Chosen items:", chosen_items)





