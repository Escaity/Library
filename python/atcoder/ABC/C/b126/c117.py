k, n = list(map(int, input().split()))
x = list(map(int, input().split()))
x.sort()
# 2点間の絶対距離を格納するリスト
df = [0] * (n - 1)
for i in range(n - 1):
    df[i] = abs(x[i + 1] - x[i])

# 距離のリストを降順に並べて、距離の遠い点を除いた点の合計距離を求める
df.sort(reverse=True)
print(sum(df[k - 1 :]))

"""
in:
2 5
10 12 1 2 14
out:
5
"""
