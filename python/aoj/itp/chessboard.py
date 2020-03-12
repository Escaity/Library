recl = []
while True:
    wh = list(map(int, input().split()))
    if sum(wh) == 0:
        break
    recl.append(wh)

for h, w in recl:
    board = [[""] * w for _ in range(h)]
    for j in range(h):
        for i in range(w):
            if (i + j) % 2 == 0:
                board[j][i] = "#"
            else:
                board[j][i] = "."
        print(*board[j], sep="")
    print()

