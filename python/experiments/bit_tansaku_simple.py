ia = [1, 2, 3, 4]
w = 4
flag = False
for x in range(1 << len(ia)):
    tot = 0
    for i in range(len(ia)):

        if x & (1 << i):
            tot += ia[i]
    if tot == w:
        flag = True
        break
print("Yes") if flag else print("No")
