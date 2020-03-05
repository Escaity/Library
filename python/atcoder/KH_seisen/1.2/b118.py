# https://atcoder.jp/contests/abc118/tasks/abc118_b
"""
3 4
2 1 3
3 1 2 3
2 3 2
"""
N, M = map(int, input().split())
K, A = [0] * N, [0] * N
for i in range(N):
    K[i], *A[i] = map(int, input().split())
k = set(i for i in range(1, M + 1))
k = k.intersection(*A)
print(len(k))
