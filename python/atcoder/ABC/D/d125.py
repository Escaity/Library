"""
負数の数が偶数ならただの足し算、
奇数なら最小の数を負数に変換して足し算すると考えた
"""
n = int(input())
a = list(map(int, input().split()))
cnt = [1 for x in a if x < 0]
ans = 0
mini = float("inf")
for i in a:
    if i < 0:
        i *= -1
    mini = min(mini, i)
    ans += i
if sum(cnt) % 2 == 0:
    print(ans)
else:
    print(ans - mini * 2)

"""
3
-10 5 -4
"""
