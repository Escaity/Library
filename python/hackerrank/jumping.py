"""
N:8
cl:0 0 0 0 1 0 1 0
cc:  1 1 1 9 1 9 1
     1 2 3 4 5 6 7
dp:0 1 1 2 10 3 12 4
"""
n = int(input())
A = list(map(int, input().split()))
a = []
for i in A:
    if i == 0:
        a.append(1)
    else:
        a.append(100)

dp = [float("inf")] * n
dp[0] = 0

for i in range(1, n):
    dp[i] = min(dp[i], dp[i - 1] + a[i - 1])
    if i > 1:
        dp[i] = min(dp[i], dp[i - 2] + a[i - 2])

print(dp[n - 1])
