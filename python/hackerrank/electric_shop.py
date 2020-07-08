def getMoneySpent(keyboards, drives, b):
    ttl, ans = 0, 0

    cantb = False
    for i in keyboards:

        for j in drives:
            if i + j <= b:
                ttl = i + j
            else:
                cantb = True
            ans = max(ans, ttl)

    if cantb == True and ans == 0:
        ans = -1
    return ans
