n, m, l = map(int, input().split())
a = [None] * n
b = [None] * m
for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(m):
    b[i] = list(map(int, input().split()))
c = [[0] * n for _ in range(l)]
for i in range(n):
    for j in range(l):
        for k in range(m):
            c[j][i] += a[j][k] * b[k][i]
for i in c:
    print(*i)
