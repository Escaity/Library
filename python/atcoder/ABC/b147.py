s = list(input())
cnt = 0
while len(s)>1:
    if s.pop(0) == s.pop(-1):
        pass
    else:
        cnt += 1
print(cnt)