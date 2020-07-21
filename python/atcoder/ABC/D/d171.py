n = int(input())
a = list(map(int, input().split()))
q = int(input())
b, c = [None] * q, [None] * q
ans = [0] * q
for i in range(q):
    b[i], c[i] = list(map(int, input().split()))
    al = list(map(lambda x: c[i] if x == b[i] else x, a))
    ans[i] = sum(al)
    a = al
for i in ans:
    print(i)

"""
4
1 2 3 4
3
1 2
3 4
2 4
out:
11
12
16
"""
