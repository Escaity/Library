# https://atcoder.jp/contests/abc095/tasks/abc095_b

N, g = list(map(int, input().split()))
k = [int(input()) for i in range(N)]
cnt = N
zan = g - sum(k)
while zan >= min(k):
    zan -= min(k)
    cnt += 1

print(cnt)
"""
n,x=map(int,input().split())
l=[int(input()) for _ in range(n)]
print(n+((x-sum(l))//min(l)))
"""
