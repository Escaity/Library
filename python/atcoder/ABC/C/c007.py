from collections import deque

H, W = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))
M = [None] * H
dist = [[-1] * W for _ in range(H)]
que = deque()
que.append((sy - 1, sx - 1))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dist[sy - 1][sx - 1] = 0

for i in range(H):
    M[i] = list(input())
M[sy - 1][sx - 1] = "#"
while que:
    v = que.popleft()
    for d in range(4):
        if v:
            h, w = int(*v[:1]), int(*v[1:])
        nh, nw = h + dy[d], w + dx[d]
        if nh < 0 or nw < 0 or nh >= H or nw >= W or M[nh][nw] == "#":
            continue
        if dist[nh][nw] != -1:
            continue
        M[nh][nw] = "#"
        dist[nh][nw] = dist[h][w] + 1
        que.append((nh, nw))


print(dist[gy - 1][gx - 1])

