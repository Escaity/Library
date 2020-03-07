# https://atcoder.jp/contests/abc115/tasks/abc115_a
D = int(input())
c = "Christmas"
e = " Eve"
print(c, end="")
if D != 25:
    for i in range(25 - D):
        print(e, end="")
print()

"""
print("Christmas"+" Eve"*(25-int(input())))
"""
