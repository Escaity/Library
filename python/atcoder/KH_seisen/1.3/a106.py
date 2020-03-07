# https://atcoder.jp/contests/abc106/tasks/abc106_a
X, Y = list(map(int, input().split()))
ans = X * Y - (X + Y - 1)
print(ans)
