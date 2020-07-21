n = int(input())
a = list(map(int, input().split()))
sa = set(a)
print("Yes") if len(a) == len(sa) else print("No")
