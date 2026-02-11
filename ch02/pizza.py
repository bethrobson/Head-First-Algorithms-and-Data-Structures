
topping_list = ["Pineapple", "Anchovies", "Chocolate", "Pickles"]

def pizza_pairings(toppings):
    pair_count = 0
    for topping1 in toppings:
        for topping2 in toppings:
            print(f"Would you try: {topping1} + {topping2} pizza?")
            pair_count += 1
    print(f"\nTotal topping combos tested: {pair_count}")

pizza_pairings(topping_list)

print("\n")

def first_two(toppings):
    pair_count = 0
    for topping1 in toppings[:2]:
        for topping2 in toppings[:2]:
            print(f"Would you try: {topping1} + {topping2} pizza?")
            pair_count += 1
    print(f"\nTotal topping combos tested: {pair_count}")

first_two(topping_list)


