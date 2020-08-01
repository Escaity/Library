x = int(input())
d = x // 100
k = d * 5
if x <= 100 * d + k:
    print(1)
else:
    print(0)

