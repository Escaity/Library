# https://atcoder.jp/contests/abc037/tasks/abc037_b
N, Q = map(int, input().split())
l, r, t = [0] * Q, [0] * Q, [0] * Q
for i in range(Q):
    l[i], r[i], t[i] = map(int, input().split())
A = [0] * N
for i in range(Q):
    for j in range(l[i] - 1, r[i]):
        A[j] = t[i]

print(*A, sep="\n")
