# Coin change problem, dynamic programming solution

def min_tokens_choice(amount, coins):
    dp = [float('inf')] * (amount + 1)
    choice = [None] * (amount + 1)

    dp[0] = 0  # base case: 0 coins to make 0

    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                candidate = dp[a - c] + 1
                if candidate < dp[a]:
                    dp[a] = candidate
                    choice[a] = c

    # reconstruct solution
    tokens = []
    a = amount
    while a > 0:
        c = choice[a]
        tokens.append(c)
        a -= c

    return dp[amount], tokens

# This version uses backtracking to reconstruct
# which coins were used for the solution
def min_tokens(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # fill dp table
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)

    if dp[amount] == float('inf'):
        return -1, []

    # backtrack to retrieve coins used
    a = amount
    tokens = []
    while a > 0:
        for c in coins:
            if c <= a and dp[a] == dp[a - c] + 1:
                tokens.append(c)
                a -= c
                break  # move to next amount

    return dp[amount], tokens

coins = [1, 7, 10]
result, which_tokens = min_tokens(14, coins)
print(f"Coins for 14: { result }, { which_tokens }")
result, which_tokens = min_tokens(10, coins)
print(f"Coins for 10: { result }, { which_tokens }")
result, which_tokens = min_tokens(7, coins)
print(f"Coins for 7: { result }, { which_tokens }")
result, which_tokens = min_tokens(15, coins)
print(f"Coins for 15: { result }, { which_tokens }")

result, which_tokens = min_tokens(9, coins)
print(f"Coins for 9: { result }, { which_tokens }")

