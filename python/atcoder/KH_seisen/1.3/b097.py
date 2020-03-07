# https://atcoder.jp/contests/abc097/tasks/abc097_b
n = int(input())
ans = 0
for b in range(int(n ** 0.5) + 1):
    for p in range(int(n ** 0.5) + 1):
        if b ** p <= n:
            if ans < b ** p:
                ans = b ** p
print(ans)
