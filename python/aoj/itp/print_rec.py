"""
in
H W
out
#
"""
recl = []
while True:
    wh = list(map(int, input().split()))
    if sum(wh) == 0:
        break
    recl.append(wh)

for i, v in recl:
    sh = ["#"] * v
    for j in range(i):
        print(*sh, sep="")
    print()