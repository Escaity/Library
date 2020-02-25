def capital_indexes(s):
    cap = []
    for i, v in enumerate(s):
        if v.isupper():
            cap.append(str(i))

    return list(map(int, cap))


word = input()
print(capital_indexes(word))
