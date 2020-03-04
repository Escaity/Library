# https://atcoder.jp/contests/abc031/tasks/abc031_b
low, high = list(map(int, input().split()))
A = [int(input()) for _ in range(int(input()))]

ans = 0
for i in A:
    if i < low:
        ans = low - i
    elif high < i:
        ans = -1
    else:
        ans = 0
    print(ans)
