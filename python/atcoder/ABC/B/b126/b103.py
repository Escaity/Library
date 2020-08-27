from collections import deque

S = list(input())
T = input()
S = deque(S)
St = S
i = 0
flag = False
while i < len(S):
    if "".join(St) == T:
        flag = True
        break
    else:
        lst = St.pop()
        St.appendleft(lst)

    i += 1
print("Yes") if flag else print("No")
