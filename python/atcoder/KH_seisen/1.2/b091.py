# https://atcoder.jp/contests/abc091/tasks/abc091_b
from collections import Counter

s = [input() for _ in range(int(input()))]
t = [input() for _ in range(int(input()))]
ans, sav = 0, 0
smc = Counter(s).most_common()
for v, i in smc:
    if v in t:
        sav = i - t.count(v)
    else:
        sav = i

    if ans < sav:
        ans = sav
if ans < 0:
    ans = 0
print(ans)
