N, D = map(int, input().split())
xy = list(list(map(int, input().split())) for _ in range(N))
a = []
b = []
ans = 0
cnt = 0
for i, v in enumerate(xy, start=1):
    j = i
    while j < len(xy):
        a = v
        b = xy[j]
        for m in range(len(a)):
            ans += (b[m] - a[m]) ** 2

        ans = ans ** 0.5
        if ans.is_integer():
            cnt += 1
        ans = 0
        j += 1
print(cnt)
