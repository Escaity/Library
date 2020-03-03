"""
11 2
"""
N, K = list(map(int, input().split()))
d = []
while N > 0:
    d.append(N % K)
    N = N // K

print(len(d))
