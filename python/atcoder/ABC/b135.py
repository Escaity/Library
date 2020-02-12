n = int(input())
s = list(map(int, input().split()))
cnt = 0
flag = False
for i in range(n):
    if s[i] == i + 1:
        cnt += 1
    if cnt >= n - 2:
        flag = True
        break

print("YES") if flag else print("NO")
