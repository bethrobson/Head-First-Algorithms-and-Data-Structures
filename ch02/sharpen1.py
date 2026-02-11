# Examples from the Sharpen exercise on page X

def print_each_letter(word):
    for letter in word:
        print(letter)

print_each_letter("test")


def count_down_by_halves(n):
    while n > 1:
        print(n)
        n = n // 2

count_down_by_halves(20)

def shout_hello(name):
    print(f"Hello, {name}!")

shout_hello("Eric")

players = ["Eric", "Elisabeth", "Michelle", "Melissa", "David"]
def hand_slap_championship(players):
    for player1 in players:
        for player2 in players:
            print(f"{player1} slaps hands with {player2}")

hand_slap_championship(players)

