"""
注意力の問題。forを使わずに答えが出せることに気付けるか。
"""

import math

a, b, n = list(map(int, input().split()))
x = min(n, b - 1)
ans = math.floor((a * x) / b) - a * math.floor(x / b)
print(ans)
