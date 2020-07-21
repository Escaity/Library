n, k = list(map(int, input().split()))
# nが絶対値(n-k)より大きいならループ
while n > abs(n - k):
    # nがk以上またはkがn以上ならnの値を最小化
    # (どちらか">="にしないと無限ループになる可能性※n==kのとき)
    if n >= k:
        n = min(n, n % k)
    elif k > n:
        n = min(n, k % n)
print(n)

"""
1000000000000000000 1
out: 0
"""
