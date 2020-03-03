N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(input())
A.sort()
print("".join(A))
