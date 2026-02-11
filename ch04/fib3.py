def fibonacciMemo(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo)
        return memo[n]

n = int(input("Enter number: "))
print(f"Fibonacci with memoization of {n}: { fibonacciMemo(n) }")

