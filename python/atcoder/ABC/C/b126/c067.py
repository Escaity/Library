"""
累積和問題。最小値を求める方程式に気付けるかがポイント
"""
import math

ans = math.inf
n = int(input())
c = list(map(int, input().split()))
acm = [0] * (n + 1)
# カードの山の累積和を求める
for i, v in enumerate(c, 1):
    acm[i] += acm[i - 1] + v

s, a = 0, acm[n]
for i in range(1, n):
    s = acm[i]
    # カードの総和の差はabs(a-2*s)で求まる
    ans = min(ans, abs((a - s) - s))

print(ans)
