n = list(input())
N = "".join(n)
ds = 0
for i in n:
    ds += int(i)
print("Yes") if int(N)%ds==0 else print("No")
