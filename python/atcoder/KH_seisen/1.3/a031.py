# https://atcoder.jp/contests/abc031/tasks/abc031_a
A, D = list(map(int, input().split()))
print(max((A + 1) * D, A * (D + 1)))
