# Collatz Conjecture
# For more, watch: https://www.youtube.com/watch?v=094y1Z2wpJg

num, n = 27, 27
counter = 0
while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    print(f"n: { n }")
    counter += 1
    if counter > 1000:
        break

print(f"For n = {num}, counter: { counter }")


