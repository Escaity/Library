#test
#-1 0 -2 1 -3 2 -4 3 -5 4
n = list(reversed(range(1,5)))
j = -1
s2 = []
for i in range(len(n)):
    if i%2:
        j += i
    else:
        j += -i
    s2 += str(n[j])

print(s2)