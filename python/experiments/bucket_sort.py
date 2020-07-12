cnt = [0] * 10
a = [1, 2, 8, 4, 5, 2]
# バケツソート
for v in a:
    cnt[v] = v
# filter(None, list)でlist内の0を除外する
cnti = list(filter(None, cnt))
print(cnti)
