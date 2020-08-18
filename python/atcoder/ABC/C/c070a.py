"""
複数の最小公倍数を求める問題
"""


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a // gcd(a, b) * b


n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
# ansの値を最大の最小公倍数に更新していく
ans = a[0]
# ansと2番目以降の数でlcmをとることで複数のlcmが求まる
for x in range(1, n):
    ans = lcm(ans, a[x])

print(ans)

"""in
5
2
5
10
1000000000000000000
1000000000000000000
out
1000000000000000000
"""
