n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if l[i] == l[j] or l[j] == l[k] or l[k] == l[i]:
                continue

            else:
                # 3角形の成立条件
                if l[i] + l[j] > l[k] and l[j] + l[k] > l[i] and l[k] + l[i] > l[j]:
                    ans += 1
print(ans)
