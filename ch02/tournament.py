def tournament_matchups(players):
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            print(f"{players[i]} vs {players[j]}")

tournament_matchups(["Ash", "Blake", "Casey", "Drew"])

