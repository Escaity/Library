# https://atcoder.jp/contests/abc028/tasks/abc028_a
N = int(input())
if N < 60:
    print("Bad")
elif N < 90:
    print("Good")
elif N < 100:
    print("Great")
elif N == 100:
    print("Perfect")
"""
print((["Bad"]*6+["Good"]*3+["Great"]+["Perfect"])[int(input())//10])
"""
