import sys

sys.setrecursionlimit(10 ** 6)
H, W = map(int, input().split())
maze = [] * H
seen = [[False] * W for _ in range(H)]
for i in range(H):
    maze.append(list(input()))

for i in range(H):
    seen[i] = list(map(lambda x: True if x == "#" else False, maze[i]))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(h, w):
    seen[h][w] = True
    for dir in range(4):
        nh = h + dx[dir]
        nw = w + dy[dir]

        if nw < 0 or nh < 0 or nw >= W or nh >= H:
            continue
        if maze[nh][nw] == "#":
            continue
        if seen[nh][nw]:
            continue

        dfs(nh, nw)


for h in range(H):
    for w in range(W):
        if maze[h][w] == "s" or maze[h][w] == "g":
            if maze[h][w] == "g":
                gx, gy = w, h
            if maze[h][w] == "s":
                stx, sty = w, h

dfs(sty, stx)

print("Yes") if seen[gy][gx] else print("No")
