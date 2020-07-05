"""
3 4 240
60 90 120
80 150 80 150
"""
from collections import deque

n, m, k = list(map(int, input().split()))
A = deque(map(int, input().split()))
B = deque(map(int, input().split()))
time = 0
read = 0
select = 0
for _ in range(n+m):
    select = min(A[0], B[0])
    if select == A[0]:
        A.popleft()
    else:
        B.popleft()
    time += select
    read += 1
    if time > k:
        read -= 1
        break
print(read)
