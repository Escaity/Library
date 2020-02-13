n = list(input())
ni = list(map(int,n))
nsum = sum(ni)
ans = 0
op = []
for i in ni:
    ans += i
    
    if nsum > 7 and ans > 7:
        ans -= i
        op += "-"
    else:
        op += "+"
print("%d%s%d%s%d%s%d=7" % (ni[0],op[0],ni[1],op[1],ni[2],op[2],ni[3]))