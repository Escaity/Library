n = int(input())
a = list(map(int, input().split()))

cnt, ans = 0, 0
"""
1 20 2 2 2
6
2 7 1 8 2 8
7 8 1 2 8 2
"""


for i in a:
    if i % 4 == 0:
        cnt += 1
