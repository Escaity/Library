"""
組み合わせ方が最大になるnCrを求める。
数列内の中間の数の求め方、n==2の時に注意
"""
n = int(input())
a = list(map(int, input().split()))
maxa = max(a)
mini = [[] for _ in range(n)]
for i, v in enumerate(a):
    r = maxa - v
    # 数列vがどれだけ中間にあるか(v - r)を格納する
    mini[i] = [v, abs(v - r)]
# maxaの中間に近い順にソート
mini.sort(key=lambda x: x[1])
if n == 2:
    # 数列aの要素数が２つなら答えは(最大、最小)
    print(maxa, min(a))
else:
    print(maxa, mini[0][0])
