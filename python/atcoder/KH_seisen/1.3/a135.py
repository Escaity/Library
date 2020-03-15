# https://atcoder.jp/contests/abc135/tasks/abc135_a
a, b = list(map(int, input().split()))
print((a + b) // 2) if (a + b) % 2 == 0 else print("IMPOSSIBLE")
