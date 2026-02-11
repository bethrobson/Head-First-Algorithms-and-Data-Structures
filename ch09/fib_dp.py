def fib_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    print(f"dp: {dp}")
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        print(f"dp: {dp}")
    return dp[n]

print(f"Fibonacci of 10: {fib_dp(10)}")


