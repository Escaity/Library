N, K, X, Y = (int(input()) for i in range(4))
"""
N = int(input())
K = int(input())
X = int(input())
Y = int(input())
"""
if N <= K:
    print(N * X)
else:
    print(K * X + (N - K) * Y)
