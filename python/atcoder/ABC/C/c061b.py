# 配列の範囲は10**5
AMAX = 100000
cnt = [0] * (AMAX + 1)

N, K = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(N)]

# バケツソートを用いる
for i in range(N):
    cnt[ab[i][0]] += ab[i][1]

for ans in range(AMAX):
    if K <= cnt[ans]:
        print(ans)
        break
    K -= cnt[ans]
