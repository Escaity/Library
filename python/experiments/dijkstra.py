"""
4 4
1 2
2 3
3 4
4 2
"""
import math
import heapq

n, m = list(map(int, input().split()))
path = [[0] * n for _ in range(n)]
for i in range(m):
    x, y = list(map(int, input().split()))
    path[x - 1][y - 1] = 1
    path[y - 1][x - 1] = 1


def dijkstra(st, W):
    dst_list = [math.inf] * len(W)
    dst_list[st] = 0
    done = []
    nextV = []
    for i, d in enumerate(dst_list):
        heapq.heappush(nextV, (d, i))
    while nextV:
        p = heapq.heappop(nextV)
        i = p[1]
        if i in done:
            continue
        done.append(i)
        for j, x in enumerate(W[i]):
            if x == 1 and j not in done:
                d = min(dst_list[j], dst_list[i] + x)
                dst_list[j] = d
                heapq.heappush(nextV, (d, j))
    return dst_list


ans = dijkstra(0, path)
print(ans)
if math.inf in ans:
    print("No")
else:
    print("Yes")
    for i in ans[1:]:
        print(i)
