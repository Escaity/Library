import itertools

n = int(input())
tako = list(map(int, input().split()))
comb = list(itertools.combinations(tako, 2))
ans = 0
for i in comb:
    ans += i[0] * i[1]

print(ans)
