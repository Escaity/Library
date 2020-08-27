import itertools

n, k = list(map(int, input().split()))
ab = [[] for _ in range(n)]
for i in range(n):
    ab[i] = list(map(int, input().split()))

# 要素を小さい順に並べておく
ab.sort(key=lambda x: x[0])
# 列の要素に分ける
az, bz = list(zip(*ab))

# b列の累積和をとることで特定の要素の番号がわかる
accb = list(itertools.accumulate(bz))
idx = 0
for j, v in enumerate(accb):
    # k番目の要素のインデックスをとったらbreak
    if k <= v:
        idx = j
        break
print(az[idx])
