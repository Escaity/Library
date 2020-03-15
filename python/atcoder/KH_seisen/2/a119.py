# https://atcoder.jp/contests/abc119/tasks/abc119_a

n = input()
f = False
year = int(n[0:4])
mon = int(n[5:7])
if year == 2019:
    if mon > 4:
        f = True
elif year > 2019:
    f = True

print("TBD") if f else print("Heisei")

"""
S=input()
print("Heisei" if S<="2019/04/30" else "TBD")
"""
