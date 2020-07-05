import itertools

s = str(input())
sg = itertools.groupby(s)
ans = []
for i, w in enumerate(sg):
    ans.append("(" + str(len(list(w[1]))) + ", " + str(w[0]) + ")")
print(ans)
