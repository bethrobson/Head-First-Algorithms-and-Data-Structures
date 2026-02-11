
def example(n):
    for x in range(3):
        print(f"Warming up... {x}")

    for y in range(2 * n):
        print(f"Scanning item... {y}")

    for i in range(n):
        for j in range(n):
            print(f"Processing pair... {i, j}")


def log_example(n):
    while n > 1:
        print(f"Almost there... n is {n}")
        n = n // 2


def compatible(n):
    for i in range(n):
        print(f"Examining {i}.")

    for round in range(3): 
       for i in range(n):
            for j in range(n):
                print(f"Testing {round}: {i} with {j}.")


example(10)

log_example(10)

compatible(10)


