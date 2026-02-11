import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacciMemo(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo)
    return memo[n]

def fibonacciIter(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(1, n):
        a, b, = b, a + b
        fibs.append(b)
    return b

n = int(input("Enter a number: "))
print(f"Fibonacci of {n}: { fibonacci(n) }")

"""
n = int(input("Enter a number: "))
start = time.time()
print(f"Fibonacci of {n}: { fibonacci(n) }")
end = time.time()
print(f"Time to run: { end-start }")

start = time.time()
print(f"Fibonacci with memoization of {n}: { fibonacciMemo(n) }")
end = time.time()
print(f"Time to run: { end-start }")

fibs = [0, 1]
start = time.time()
print(f"Fibonacci with iteration of {n}: { fibonacciIter(n) }")
end = time.time()
print(f"Time to run: { end-start }")
print(fibs)
"""

