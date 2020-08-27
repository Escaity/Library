import math

n = int(input())
t = [0] * 5
for i in range(5):
    t[i] = int(input())
print(math.ceil(n / min(t)) + 4)

"""
10000000007
2
3
5
7
11
"""
