"""
探索範囲を絞ることが重要
"""
import sys

n = int(input())
for a in range(-200, 201):
    for b in range(-200, 201):
        if a * a * a * a * a - b * b * b * b * b == n:
            print(a, b)
            sys.exit(0)
