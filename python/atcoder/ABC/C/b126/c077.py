"""
二分探索を用いる
"""

import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))
ans = 0
for i in b:
    # 中韓より小さい数がaに何個あるか
    an = bisect.bisect_left(a, i)
    # 中韓より大きい数がcに何個あるか
    cn = n - bisect.bisect_right(c, i)
    # 各組み合わせの足し算
    ans += an * cn

print(ans)
