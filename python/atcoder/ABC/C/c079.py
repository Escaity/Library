n = input()
# bit前探索(オペランドの組み合わせの数だけループ)
for x in range(1 << 3):
    # オペランド初期化
    opr = ["-"] * 3
    # オペランドのパターン作成
    for i in range(3):
        if x & (1 << i):
            opr[i] = "+"
    # オペランドパターンと番号を組み合わせた式(shiki)
    shiki = "%s%s%s%s%s%s%s" % (n[0], opr[0], n[1], opr[1], n[2], opr[2], n[3])
    if eval(shiki) == 7:
        print("%s=7" % shiki)
        break
