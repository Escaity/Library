# math内のfactorial()を使う
from math import factorial

MOD = 10 ** 9 + 7
n, m = list(map(int, input().split()))
ptn = 1
# 犬と猿の数の差が2以上ならパターン無し
if abs(n - m) >= 2:
    ptn = 0
else:
    ptn = factorial(n) * factorial(m)
    # 犬と猿の数が等しい時は反転パターン分を足す（x2する)
    if abs(n - m) == 0:
        ptn *= 2

print(ptn % MOD)

"""
100000 100000
"""
