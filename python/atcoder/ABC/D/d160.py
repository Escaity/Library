from collections import deque

n, x, y = list(map(int, input().split()))
m = [[] for _ in range(n)]
m[x - 1].append(y - 1)
m[y - 1].append(x - 1)
for i in range(n - 1):
    m[i].append(i + 1)
    m[i + 1].append(i)

for j in range(n):
    seen = [False] * n
    que = deque()
    que.append(0)
    while que:
        