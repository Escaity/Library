from collections import deque

N = int(input())
a = list(map(int, input().split()))
a.sort()
a = deque(a)
print(a.pop() - a.popleft())
