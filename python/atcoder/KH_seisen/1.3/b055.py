# https://atcoder.jp/contests/abc055/tasks/abc055_b
MOD = 10 ** 9 + 7
n = int(input())
ans = 1
a = (i for i in range(1, n + 1))
for i in a:
    ans = ans * i % MOD
print(ans)
   