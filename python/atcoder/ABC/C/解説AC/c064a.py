n = int(input())
s = list(map(int, input().split()))
rate = [0]*9
cntz = ""
for i in range(n):
    if s[i]>=3200:
        rate[8] += 1
        continue
    else:
        rate[s[i]//400] = 1

if rate[8] > 0:
    cntz = "".join(map(str,rate))
    cntz = cntz.replace("0","")
    if len(cntz) == 1:
        print(1,sum(rate))
    else:
        print(sum(rate)-rate[8],sum(rate))
else:
    print(sum(rate), sum(rate))
