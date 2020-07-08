H, W, K = list(map(int, input().split()))
tile = [""] * H
for i in range(H):
    tile[i] = list(input())

ans = 0
# bit前探索
for ti in range(1 << H):
    for tj in range(1 << W):
        cnt = 0
        for i in range(H):
            for j in range(W):
                if ti >> i & 1:
                    print("passR:%s" % bin(ti))
                    continue
                if tj >> j & 1:
                    print("passC:%s" % bin(tj))
                    continue
                if tile[i][j] == "#":
                    print("tile[%d][%d]" % (i, j))
                    cnt += 1
        if cnt == K:
            ans += 1
            print("ans: %d" % ans)
        print("next")
print(ans)
