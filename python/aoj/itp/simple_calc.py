ans = []
while True:
    a = input()
    end = a.find("?")
    if end != -1:
        break
    ans.append(int(eval(a)))
print(*ans, sep="\n")