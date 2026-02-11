def greedy_change(amount, coins):
    coins = sorted(coins, reverse=True)
    change = []
    amounts = [amount]

    for coin in coins:
        while amount >= coin:
            amount -= coin
            amounts.append(amount)
            change.append(coin)

    return change, amounts

coins = [25, 10, 5, 1]
change, amounts = greedy_change(67, coins)
print(f"Amounts: { amounts }")
print(f"Change: { change }")

coins = [4, 3, 1]
change, amounts = greedy_change(6, coins)
print(f"Amounts: { amounts }")
print(f"Change: { change }")

