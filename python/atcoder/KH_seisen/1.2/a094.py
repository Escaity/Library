# https://atcoder.jp/contests/abc094/tasks/abc094_b

N, M, X = map(int, input().split())
A = list(map(int, input().split()))
arr = [0] * (N + 1)
for i in A:
    arr[i] = 1
l, r = sum(arr[:X]), sum(arr[X + 1 :])
print(min(l, r))
