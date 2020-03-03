from collections import deque

N = int(input())
a = deque(map(int, input().split()))
l, r = 0, 0
while a:
    if l <= r:
        l += a.popleft()
    else:
        r += a.pop()
print(abs(l - r))
