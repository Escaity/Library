"""
幅優先探索を用いた解法
"""
from collections import deque

h, w = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
M = [[] for _ in range(h)]
for i in range(h):
    M[i] = input()
# 探索済み領域の保存＋スタートからの距離を保管する
seen = [[0] * w for _ in range(h)]
que = deque()
# 始点をqueに格納
que.append((sx - 1, sy - 1))
while que:  # queが残っているならループ
    X, Y = que.popleft()  # 現在の(x, y)座標を取得
    D = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 4方向の動きをさせるための配列
    for dx, dy in D:  # 現在地点から4方向に動かして探索
        # 動いた座標が"."で未探索領域なら
        if M[X + dx][Y + dy] == "." and seen[X + dx][Y + dy] == 0:
            # 始点からその座標までの距離を格納
            seen[X + dx][Y + dy] = seen[X][Y] + 1
            # 探索した座標を次の現在地候補にする
            que.append((X + dx, Y + dy))
            

print(seen[gx - 1][gy - 1])

"""in
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########
out: 11
"""
