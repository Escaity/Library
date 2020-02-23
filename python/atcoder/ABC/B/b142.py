n, height = map(int, input().split())
hl = list(map(int, input().split()))
cnt = 0
for i in hl:
    if height <= i:
        cnt += 1

print(cnt)