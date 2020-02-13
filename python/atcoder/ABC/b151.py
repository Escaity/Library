N, K, target = list(map(int, input().split()))
grade = list(map(int, input().split()))
for i in range(K + 1):
    if target <= (sum(grade) + i) // N:
        print(i)
        break
    elif i == K:
        print(-1)
