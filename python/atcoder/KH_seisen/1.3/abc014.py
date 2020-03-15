# https://atcoder.jp/contests/abc014/tasks/abc014_1
s = int(input())
n = int(input())
cnt = 0
if s % n == 0:
    print(0)
else:
    while True:
        cnt += 1
        if (s + cnt) % n == 0:
            print(cnt)
            break

