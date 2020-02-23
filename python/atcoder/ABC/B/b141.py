S = list(input())
odd, even = [], []
for i, v in enumerate(S):
    if i % 2 == 0:
        if v == "R" or v == "U" or v == "D":
            continue
        else:
            odd.append(v)
            break

    else:
        if v == "L" or v == "U" or v == "D":
            continue
        else:
            even.append(v)
            break

print("No") if odd or even else print("Yes")
