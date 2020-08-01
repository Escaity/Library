"""
深さ優先探索(dfs)を使う
"""
n, m = map(int, input().split())
t = [[] for _ in range(n)]
# グラフを作成
for _ in range(m):
    a, b = map(int, input().split())
    t[a - 1].append(b - 1)
    t[b - 1].append(a - 1)
# 探索済み頂点を格納するリスト
visited = [False] * n


def dfs(now, depth):
    # 現在地が探索済みなら0を返す
    if visited[now]:
        return 0
    # 終点に着いたら1を返す
    if depth == n - 1:
        return 1

    # 現在地を探索済みにする
    visited[now] = True
    # 条件を満たす回数を格納する
    ans = 0

    # 作成したグラフの経路をループで回す
    for e in t[now]:
        # 次の経路(e)の中で探索してない場所があるとき
        if not visited[e]:
            # dfsで更に深いところへ進む
            ans += dfs(e, depth + 1)
    # 探索領域を現在位置にまで戻す
    visited[now] = False
    return ans


print(dfs(0, 0))
