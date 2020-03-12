"""
W H x y r
5 4 2 2 1
Yes
"""
w, h, x, y, r = list(map(int, input().split()))
xl, yl = x - r, y - r
xr, yr = x + r, y + r
if 0 <= xl and 0 <= yl and xr <= w and yr <= h:
    print("Yes")
else:
    print("No")
