n = int(input())
m = [list(map(int, input().split())) for _ in range(2)]
dp = [[0] * n for _ in range(2)]
dp[0][0] = m[0][0]
dp[1][0] = m[0][0] + m[1][0]
for i in range(1, n):
    dp[0][i] = dp[0][i - 1] + m[0][i]
    dp[1][i] = max(dp[0][i], dp[1][i - 1]) + m[1][i]

print(dp[1][n - 1])

