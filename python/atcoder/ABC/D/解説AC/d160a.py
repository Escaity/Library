n, x, y = map(int, input().split())

dl = [0] * (n - 1)
for i in range(1, n):
    for j in range(i + 1, n + 1):
        dist = min(j - i, abs(i - x) + 1 + abs(j - y))
        dl[dist - 1] += 1
for i in dl:
    print(i)
