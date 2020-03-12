n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
ans = [0] * 3
dxy = 0
for i in range(3):
    xy = list(map(lambda a, b: abs(b - a) ** (1 + i), x, y))
    ir = 1 / (i + 1)
    dxy = sum(xy) ** ir
    ans[i] = dxy
for j in ans:
    print(j)
print(max(map(lambda a, b: abs(b - a), x, y)))
