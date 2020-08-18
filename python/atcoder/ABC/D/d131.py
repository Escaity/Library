n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
# 二次元配列abの配列2番目の要素を昇順にソートする
ab.sort(key=lambda x: x[1])
# 累積時間を格納する変数r
r = 0
flag = True
for a, b in ab:
    r += a
    # 累積時間が締め切り時間を超えた場合はFalseを返す
    if r > b:
        flag = False
        break

print("Yes") if flag else print("No")

"""in
5
2 4
1 9
1 8
4 9
3 12
out:
Yes
"""
