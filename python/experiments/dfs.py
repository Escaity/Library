from collections import deque

v, e = map(int, input().split())
s, t = map(int, input().split())
m = [[] for _ in range(v)]
for i in range(e):
    a, b = map(int, input().split())
    m[a].append(b)

seen = [False] * v
st = deque()
st.append(s)
seen[s] = True

while st:
    n = st.pop()
    for nx in m[n]:
        if seen[nx] is False:
            seen[nx] = True
            st.append(nx)

if seen[t]:
    print("Yes")
else:
    print("No")
