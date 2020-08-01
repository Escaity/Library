x1, v1, x2, v2 = list(map(int, input().split()))
x, y = [x1], [x2]
i = 0
flag = False
while x[i] <= 100 or y[i] <= 100:
    i += 1
    x.append(x[i - 1] + v1)
    y.append(y[i - 1] + v2)
    if x[i] == y[i]:
        flag = True
        break
if flag:
    print("YES")
else:
    print("NO")
