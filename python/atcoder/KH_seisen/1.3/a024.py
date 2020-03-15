# https://atcoder.jp/contests/abc024/tasks/abc024_a
"""
100 200 50 20
40 10
"""
a, b, c, k = map(int, input().split())
s, t = map(int, input().split())
disc = 0
if s + t >= k:
    disc = c * (s + t)
ans = a * s + b * t - disc
print(ans)
