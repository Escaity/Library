# https://atcoder.jp/contests/abc158/tasks/abc158_b

n, b, r = map(int, input().split())
div = n // (b + r)
base = b * div
zan = n % (b + r)
ama = min(zan, b)
print(base + ama)
