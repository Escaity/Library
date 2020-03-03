a = list(map(str, input().split()))
a.sort(reverse=True)
num = a[0] + a[1]
num = "".join(num)
print(int(num) + int(a[2]))
"""
A,B,C=sorted(map(int,input().split()))
print(10*C+B+A)
"""
