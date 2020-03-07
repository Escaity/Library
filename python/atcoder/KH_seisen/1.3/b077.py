# https://atcoder.jp/contests/abc077/tasks/abc077_b
n = int(input())
ans = 0
for i in range(int(n ** 0.5) + 1):
    if i ** 2 <= n:
        if ans < i ** 2:
            ans = i ** 2
print(ans)

