from collections import Counter

f = True
s = Counter(input())
for i in s.values():
    if i % 2 != 0:
        f = False

print("Yes") if f else print("No")

"""in
abaccaba
out:
Yes
"""
