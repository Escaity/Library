n = int(input())
sq = 0
for i in range(1, n + 1):
    if n == 1:
        print(1)
        break
    sq = i**2
    if sq > n:
        print((i - 1)**2)
        break
    else:
        pass
