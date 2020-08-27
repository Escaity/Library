"""
累積和を用いた解法
"""
n, q = list(map(int, input().split()))
s = input()
# i+1で走査するため要素数+1する
t = [0] * (n + 1)
# ACの文字列を見つけたら配列の要素＋１していく
for i in range(n):
    t[i + 1] = t[i] + (1 if s[i : i + 2] == "AC" else 0)

for i in range(q):
    # 区間を受け取り"AC"の数を返す
    l, r = map(int, input().split())
    print(t[r - 1] - t[l - 1])

"""in
8 3
ACACTACG
3 7
2 3
1 8
"""
