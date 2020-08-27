n, m = list(map(int, input().split()))
w = [0] * n
for i in range(m):
    a, b = list(map(int, input().split()))
    w[a - 1] += 1
    w[b - 1] += 1

for i in w:
    print(i)
