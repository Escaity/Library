# https://atcoder.jp/contests/arc008/tasks/arc008_1
N = int(input())

print(N // 10 * 100 + min(100, N * 15))
