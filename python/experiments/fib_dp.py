def fib(n):
    dp = [None] * n
    dp[0] = 0
    dp[1] = 1

    for i in range(n - 2):
        dp[i + 2] = dp[i] + dp[i + 1]

    return dp[n - 1]


print(fib(5))
