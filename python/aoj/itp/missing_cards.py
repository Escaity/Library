n = int(input())
sp, ht, cl, di = [0] * 13, [0] * 13, [0] * 13, [0] * 13
temp = [""] * 2
for i in range(n):
    temp = input().split()
    if temp[0] == "S":
        sp[int(temp[1]) - 1] = True
    if temp[0] == "H":
        ht[int(temp[1]) - 1] = True
    if temp[0] == "C":
        cl[int(temp[1]) - 1] = True
    if temp[0] == "D":
        di[int(temp[1]) - 1] = True
for i, v in enumerate(sp, start=1):
    if v == 0:
        print("S %d" % i)
for i, v in enumerate(ht, start=1):
    if v == 0:
        print("H %d" % i)
for i, v in enumerate(cl, start=1):
    if v == 0:
        print("C %d" % i)
for i, v in enumerate(di, start=1):
    if v == 0:
        print("D %d" % i)
