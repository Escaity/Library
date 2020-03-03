from collections import deque

o = deque(list(input()))
e = deque(list(input()))
pas = []
while o or e:
    if o:
        pas.append(o.popleft())
    if e:
        pas.append(e.popleft())

print(*pas, sep="")
