import numpy as np

n, m, x = map(int, input().split())
a = [None] * n
cost = 0
ans = float("inf")
# 本の要素を入力
for i in range(n):
    a[i] = list(map(int, input().split()))
# bit前探索
for bit in range(1, 1 << n):
    # 組み合わせパターンと理解度の合計を初期化
    ptn = []
    psum = [0]
    for i in range(n):
        if bit & 1 << i:
            ptn.append(a[i])
            # 取り出したパターン列を一括足し算
            psum = np.sum(ptn, axis=0)
    cost = psum[0]
    # 理解度の条件を満たした時はcostを取得し、最小値を求める
    if np.min(psum[1:]) >= x:
        ans = min(ans, cost)
# costが更新されなければ（答えがない）-1を出力
print(-1) if ans == float("inf") else print(ans)
