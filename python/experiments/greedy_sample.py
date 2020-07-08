k = [1, 5, 10, 50, 100, 500]
change = 1000 - int(input())
coin, cnt = 0, 0
while change > 0:
    k = list(map(lambda x: x if x <= change else 0, k))
    coin = change // max(k)
    cnt += coin
    change -= coin * max(k)
print(cnt)
