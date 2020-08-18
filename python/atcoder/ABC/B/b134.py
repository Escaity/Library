"""
20 4
"""
import math

n, d = list(map(int, input().split()))
print(math.ceil(n / (d * 2 + 1)))

