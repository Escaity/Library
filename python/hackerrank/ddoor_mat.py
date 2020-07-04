x, y = list(map(int, input().split()))
dia = ".|."
slash = "-"
for i in range(0, x // 2):
    print(slash * (y // 2 - 3 * i - 1), end="")
    print(dia * (2 * i + 1), end="")
    print(slash * (y // 2 - 3 * i - 1))
print(slash * ((y - 7) // 2), end="")
print("WELCOME", end="")
print(slash * ((y - 7) // 2))
for i in range(0, x // 2)[::-1]:
    print(slash * (y // 2 - 3 * i - 1), end="")
    print(dia * (2 * i + 1), end="")
    print(slash * (y // 2 - 3 * i - 1))

