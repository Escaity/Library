H, N = map(int,input().split())
waza = map(int,input().split())

print("Yes") if H <= sum(waza) else print("No")
