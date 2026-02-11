import math

def algorithm1(number):
    high = 100
    for i in range(1, high):
        print(f"Guessing {i}")
        if i == number:
            print(f"You guessed the number {number} in {i} guesses")
            break

def algorithm2(high, number):
    low = 1
    found = False
    guesses = 0
    while not found:
        guesses = guesses + 1
        mid = (low + high) // 2
        print(f"Guessing {mid}")
        if mid == number:
            print(f"You guessed the number {number} in {guesses} guesses")
            found = True
        elif mid < number:
            low = mid + 1
        else:
            high = mid - 1

try:
	high = int(input("Enter high number for range: "))
	secret = int(input("Enter secret number: "))
	algorithm2(high, secret)
	print(f"Log base 2 of {high}: {math.log2(high)}")
except ValueError:
	print("Invalid input! Please enter a valid number.")
