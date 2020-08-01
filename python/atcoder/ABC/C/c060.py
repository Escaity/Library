import math

n, t = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
a.append(math.inf)
for i in range(n):
    # シャワーの時間か次の人がスイッチを押す時間か
    ans += min(t, a[i + 1] - a[i])
print(ans)
