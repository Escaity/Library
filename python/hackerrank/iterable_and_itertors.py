import itertools

al = []
count = 0
N = int(input())
a = input().replace(" ", "")
K = int(input())
al.extend(list(itertools.combinations(a, K)))
for i in al:
    if "a" in i:
        count += 1
print(count / len(al))
