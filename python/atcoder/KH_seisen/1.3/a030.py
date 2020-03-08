# https://atcoder.jp/contests/abc030/tasks/abc030_a
a, b, c, d = list(map(int, input().split()))
t = float(b / a)
a = float(d / c)
if t == a:
    print("DRAW")
else:
    print("TAKAHASHI") if t > a else print("AOKI")
