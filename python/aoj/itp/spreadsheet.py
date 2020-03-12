x, y = map(int, input().split())
sheet = []
for i in range(x):
    sheet.append(list(map(int, input().split())))
for i, v in enumerate(sheet):
    sheet[i].append(sum(v))
sheetr = list(map(list, zip(*sheet)))
colsum = [0] * (y + 1)
for i, v in enumerate(sheetr):
    colsum[i] = sum(v)
for i in sheet:
    print(*i)
print(*colsum)
