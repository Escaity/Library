N = int(input())
a = list(map(int, input().split()))
el = []
for i in a:
    if i % 2 == 0:
        el.append(i)

for i in range(len(el)):
    if el[i] % 3 == 0 or el[i] % 5 == 0:
        el[i] = True
    else:
        el[i] = False

if el.count(False):
    print("DENIED") 
else:
    print("APPROVED")
