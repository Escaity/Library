card, sav = [], []
i, cnt = -1, 0
while True:
    s = input()
    shf, p = 0, []
    if s == "-":
        break
    elif s.isalpha():
        cnt = int(input())
        card.append(s)
        i += 1
    elif card[i]:
        pr = card[i][int(s) :]
        pl = card[i][: int(s)]
        pr += pl
        card[i] = pr

for w in range(i + 1):
    print(card[w])
