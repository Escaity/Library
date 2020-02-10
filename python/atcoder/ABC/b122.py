f = []
for w in input():
    if w == "A" or w == "C" or w == "G" or w == "T":
        f += "1"
    else:
        f += " "
if "1" in f:
    acgt = [i for i in list("".join(f).split())]
    acgt.sort()
    print(len(acgt[-1]))
else:
    print(0)