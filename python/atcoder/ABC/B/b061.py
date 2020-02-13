from collections import Counter
city, road = list(map(int, input().split()))
road_list = [list(map(int, input().split())) for _ in range(road)]
rl2 = []
for i in road_list:
    rl2.extend(i)

print(rl2)
rl2cnt = Counter(rl2)
rl2cs = sorted(rl2cnt.items())
for i in rl2cs:
    print(i[1])
