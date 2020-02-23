N = int(input())
Temp, A = list(map(int, input().split()))
H = list(map(float, input().split()))
z = [abs((Temp - x * 0.006) - A) for x in H]
print(z.index(min(z)) + 1)
