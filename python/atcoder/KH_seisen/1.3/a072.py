# https://atcoder.jp/contests/abc072/tasks/abc072_a
X, t = list(map(int, input().split()))
zan = X - t
if X - t < 0:
    zan = 0
print(zan)
