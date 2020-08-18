"""
うまくソートしてaとcの要素比較をする。多次元配列の要素番号の決め方が難しかった。
"""
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
c = [[] for _ in range(m)]
for i in range(m):
    c[i] = list(map(int, input().split()))
a.sort()
# 多次元配列cの2番目の要素で降順に並べる
c.sort(key=lambda x: x[1], reverse=True)
# 回答の初期値は配列aの合計にしておく
ans = sum(a)
# 多次元配列cの位置を格納
c0 = 0
# 配列c[x][0]の累積和を格納する
r = c[0][0]
for i, v in enumerate(a):
    # 配列cと配列aのインデックスを比較、aの番号がcの範囲を超えていたら、cの次の配列の要素数を加算
    if r <= i and c0 <= m - 2:
        c0 += 1
        r += c[c0][0]
    # 配列cが存在してかつ、cの要素 > aの要素の時にansにその差分を足す
    if r > i and v < c[c0][1]:
        ans += abs(c[c0][1] - v)
    else:
        break
print(ans)

"""in
11 3
1 1 1 1 1 1 1 1 1 1 1
3 1000000000
4 1000000000
3 1000000000

"""
