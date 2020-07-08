fruits = [["orange", 100], ["apple", 200], ["grape", 300]]
ptn = []
pair = []
bgt = 300
for x in range(1 << len(fruits)):
    tot = 0
    pair.clear()
    for i in range(len(fruits)):
        if x & (1 << i):
            tot += fruits[i][1]
            pair.append(fruits[i][0])
    if tot == bgt:
        ptn.append(list(pair))
for i in ptn:
    print(", ".join(i))
