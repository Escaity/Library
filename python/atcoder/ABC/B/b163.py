n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

if sum(a) > n:
    print(-1)
else:
    print(n - sum(a))

"""
10 2
5 6
"""
