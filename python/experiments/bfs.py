from collections import deque

# グラフの頂点v,辺e
v, e = list(map(int, input().split()))
# 開始地点s,終点t
s, t = list(map(int, input().split()))
# グラフの隣接リスト
g = [[] for _ in range(v)]
for i in range(e):
    a, b = list(map(int, input().split()))
    g[a].append(b)

# 探索済みならTrueを格納する
seen = [False] * v
# 次の探索領域を格納する
que = deque()
# 開始地点を最初に追加、seenも探索済みにする
que.append(s)
seen[s] = True

while len(que) != 0:  # 次の探索領域が存在すれば
    state = que.popleft()  # 探索する場所を格納
    for nx in g[state]:
        if seen[nx] is False:  # 探索した場所が未探索なら
            seen[nx] = True  # 探索済みにする
            que.append(nx)  # 探索した所を次の探索場所につなげる
# 終点までたどり着ければ"yes"
if seen[t]:
    print("yes")
else:
    print("no")
