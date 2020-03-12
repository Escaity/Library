s = input()
n = int(input())
sav = ""
for i in range(n):
    op = input().split()
    if op[0] == "replace":
        sl, sr = s[: int(op[1])], s[int(op[2]) + 1 :]
        s = sl + op[3] + sr

    elif op[0] == "reverse":
        r = s[int(op[1]) : int(op[2]) + 1][::-1]
        sl, sr = s[: int(op[1])], s[int(op[2]) + 1 :]
        s = sl + r + sr
    elif op[0] == "print":
        print(s[int(op[1]) : int(op[2]) + 1])

