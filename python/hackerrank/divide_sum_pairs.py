# Complete the divisibleSumPairs function below.
"""
input
6 3
1 3 2 6 1 2
out
5
"""


def divisibleSumPairs(n, k, ar):
    count = 0
    r = 1
    for l in range(n - 1):
        while r < n:
            if (ar[l] + ar[r]) % k == 0:
                count += 1
            r += 1
        r = l + 2
    return count
