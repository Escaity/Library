n = int(input())
A = list(map(int, input().split()))
t = 0
for i in A:
    t += 1/i

print(1/t)    