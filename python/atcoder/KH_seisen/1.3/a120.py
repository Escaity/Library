# https://atcoder.jp/contests/abc120/tasks/abc120_a
a, b, c = map(int, input().split())
if b // a >= c:
    print(c)
else:
    print(b // a)
