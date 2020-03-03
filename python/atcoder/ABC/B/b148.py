n = int(input())
s1, s2 = list(map(str, input().split()))
for i in range(n):
    print(s1[i] + s2[i], end="")
print()