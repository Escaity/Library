# https://atcoder.jp/contests/abc035/tasks/abc035_a
w, h = map(int, input().split())
print("16:9" if w * h % 144 == 0 else "4:3")
