from bisect import bisect_left

N, M = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
time, cnt = 0, 0
while True:
    l_a = bisect_left(A, time)
    if l_a == N:
        break
    time = A[l_a] + X
    l_b = bisect_left(B, time)
    if l_b == M:
        break
    time = B[l_b] + Y
    cnt += 1
print(cnt)
"""
3 4
2 3
1 5 7
3 8 12 13
"""
