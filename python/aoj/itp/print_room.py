recl = []
while True:
    wh = list(map(int, input().split()))
    if sum(wh) == 0:
        break
    recl.append(wh)

for i, v in recl:
    sh = ["."] * v
    shf = ["#"] * v
    for j in range(i):
        if j == 0 or j == i - 1:
            print(*shf, sep="")
        else:
            sh[0], sh[-1] = "#", "#"
            print(*sh, sep="")
    print()
