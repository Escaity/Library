"""
尺取り法
"""
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
r = 0
ttl = 0
ans = 0
# 外側のループで左側lを進める
for l in range(n):
    # 内側のループで右側rを進める
    while ttl < k:
        # 右側が要素の末尾に達したらブレーク
        if r == n:
            break
        else:
            # 合計ttlが条件kを超えなければ右側の要素を足していく
            ttl += a[r]
            r += 1
    # 右側の要素全部足してもkに届かないならループ終了
    if ttl < k:
        break
    # 見つかれば連続した要素を全て足す
    ans += n - r + 1
    # 一番左側の要素を削ぐ
    ttl -= a[l]

print(ans)
