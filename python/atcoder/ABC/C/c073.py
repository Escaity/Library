from collections import Counter

N = int(input())
d_list = [int(input()) for _ in range(N)]
dlc = Counter(d_list)
ans = 0
for i in dlc.values():
    if i % 2 == 0:
        pass
    else:
        ans += 1

print(ans)
