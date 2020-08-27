a = "abcdefghijklmnopqrstuvwxyz"
s = set(input())
c = 0

for i in s:
    a = a.replace(i,"")
    c += 1
if c < 26:
    print(a[0])
else:
    print("None")