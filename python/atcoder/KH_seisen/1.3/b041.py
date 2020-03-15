# https://atcoder.jp/contests/abc041/tasks/abc041_b

import sys

input = sys.stdin.readline
MOD = 10 ** 9 + 7
c = [0] * 3
c[0], c[1], c[2] = map(int, input().split())
c.sort()
M = (c[0] * c[1] * c[2]) % MOD
print(M)
