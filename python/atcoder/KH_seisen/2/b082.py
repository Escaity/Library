# https://atcoder.jp/contests/abc082/tasks/abc082_b

"""
ratcode
atlas
"""
s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)
if "".join(s) < "".join(t):
    print("Yes")
else:
    print("No")

"""
s=sorted(input())
t=sorted(input())[::-1]
print("Yes" if s<t else "No")
"""
