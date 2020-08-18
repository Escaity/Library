s = list(input())
c = s.count("R")
if c == 3:
    print(3)
elif c == 2 and s[1] != "S":
    print(2)
elif c == 0:
    print(0)
else:
    print(1)
