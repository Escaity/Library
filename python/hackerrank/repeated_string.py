def repeatedString(s, n):
    # 文字列中の"a"をカウント
    ac = s.count("a")
    sl = len(s)
    div = n // sl
    amari = n % sl
    sa, sac = 0, 0
    # 文字列数がnで割り切れないなら余った文字列を追加して"a"をカウント
    if amari != 0:
        sa = s[:amari]
        sac = sa.count("a")
    return ac * div + sac
