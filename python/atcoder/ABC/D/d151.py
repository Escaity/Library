"""
幅優先探索。探索領域はvisited(True,False)では
なくdist(距離)を用いて解く
"""

from collections import deque


def bfs(i, j):
    dist = [[0] * w for _ in range(h)]
    q = deque()
    q.append((i, j))
    dist[i][j] = 1  # スタート地点を探索済みにする
    while q:
        nx, ny = q.pop()
        for dx, dy in D:
            X, Y = nx + dx, ny + dy
            if X < 0 or Y < 0 or X >= h or Y >= w:
                continue
            if m[X][Y] == "#":
                continue
            if dist[X][Y] != 0:
                continue

            q.appendleft((X, Y))
            dist[X][Y] = 1 + dist[nx][ny]
    mx = 0
    # スタートから最も長い探索距離をmxに代入
    for i in dist:
        mx = max(mx, max(i))
    return mx


h, w = map(int, input().split())
m = [input() for _ in range(h)]
D = [(-1, 0), (0, -1), (1, 0), (0, 1)]
ans = 0
# スタート地点を前探索
for i in range(h):
    for j in range(w):
        if m[i][j] == ".":
            # スタートとゴールが最も遠い道筋をansに代入
            ans = max(ans, bfs(i, j))

print(ans - 1)

"""in
3 5
...#.
.#.#.
.#...
out
10
"""
