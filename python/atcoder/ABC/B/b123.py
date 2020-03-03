M = list(int(input()) for _ in range(5))
Ms = list(map(str, M))
M1 = []
lastM = 0
time = 0
for i in Ms:
    if i[-1] != "0":
        M1.append(i[-1])
    elif i[-1] == "0":
        M1.append("9")
lastM = M1.index(str(min(map(int, M1))))
last = M.pop(lastM)
for i in M:
    if i % 10 == 0:
        time += i
    else:
        time += (i // 10) * 10 + 10
print(time + last)

