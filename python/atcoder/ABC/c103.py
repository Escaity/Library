n = int(input())
s = list(map(int,input().split()))
ans = 0
for i in s:
    ans += i-1
print(ans)