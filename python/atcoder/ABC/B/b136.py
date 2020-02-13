s = input()
sd = int(s)
sl = len(s)
ans = 0
if sl == 1:
    ans += sd
if sl == 2:
    ans += 9
if sl == 3:
    ans += sd - 99 + 9
if sl == 4:
    ans += 900 + 9
if sl == 5:
    ans += sd - 9999 + 900 + 9
if sl == 6:
    ans += 90000 + 900 + 9


print(ans)
