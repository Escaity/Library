# https://atcoder.jp/contests/abc123/tasks/abc123_a

import sys

*A, k = (int(input()) for _ in range(6))
dist = 0
for i, v in enumerate(A):
    for j in A[i:]:
        dist = j - v
        if dist > k:
            print(":(")
            sys.exit()

print("Yay!")
