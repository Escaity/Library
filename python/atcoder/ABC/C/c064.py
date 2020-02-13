n = int(input())
s = list(map(int, input().split()))
a = [0]*9
c = ""
mn = 400
mx = 399
for i in s:
    if 1 <= i <= mx:
        a[0] = 1
    elif mn <= i <= mx+mn:
        a[1] = 1
    elif mn*2 <= i <= mx+mn*2:
        a[2] = 1
    elif mn*3 <= i <= mx+mn*3:
        a[3] = 1
    elif mn*4 <= i <= mx+mn*4:
        a[4] = 1
    elif mn*5 <= i <= mx+mn*5:
        a[5] = 1
    elif mn*6 <= i <= mx+mn*6:
        a[6] = 1
    elif mn*7 <= i <= mx+mn*7:
        a[7] = 1
    elif  mn*8 <= i <= mn*12:
        a[8] += 1

if a[8] > 0:
    c = "".join(map(str,a))
    c = c.replace("0","")
    if len(c) == 1:
        print(1,sum(a))
    else:
        print(sum(a)-a[8],sum(a))
elif a[8] == 0:
    print(sum(a), sum(a))