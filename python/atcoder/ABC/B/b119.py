N = int(input())
a = [list(map(str, input().split())) for i in range(N)]
a = list(map(list, zip(*a)))
ans = 0
for i, v in enumerate(a[1]):
    if v == "JPY":
        ans += int(a[0][i])
    else:
        ans += float(a[0][i]) * 380000

print(ans)
