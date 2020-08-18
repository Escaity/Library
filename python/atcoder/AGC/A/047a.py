from decimal import Decimal

n = int(input())
a = [0] * n
for x in range(n):
    a[x] = Decimal(input())
flag = False
cnt = 0
for i, v in enumerate(a, start=1):
    if i == n:
        continue
    for j in range(i, n):
        ans = str(v * a[j])
        try:
            idx = ans.index(".")
        except ValueError:
            idx = len(ans)
        try:
            f = int(float(ans[idx + 1 :]))
        except ValueError:
            pass
        if f == 0:
            cnt += 1

print(cnt)
