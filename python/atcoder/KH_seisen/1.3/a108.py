# https://atcoder.jp/contests/abc108/tasks/abc108_a

n = int(input())
if n % 2 != 0:
    print(n // 2 * (n // 2 + 1))
else:
    print((n // 2) ** 2)

