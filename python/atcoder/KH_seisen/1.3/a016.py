# https://atcoder.jp/contests/abc016/tasks/abc016_1
m, d = map(int, input().split())
f = False
if m >= d:
    if m % d == 0:
        f = True
print("YES") if f else print("NO")
