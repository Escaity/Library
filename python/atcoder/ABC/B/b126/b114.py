n = int(input())
sn = str(n)
n3 = 0
minx = 0
temp = 754
for i in range(len(str(n // 100))):
    n3 = int(sn[i : i + 3])
    minx = abs(753 - n3)
    if temp > minx:
        temp = minx

print(temp)
