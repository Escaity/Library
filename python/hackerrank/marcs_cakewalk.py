def marcsCakewalk(calorie):

    cs = sorted(calorie)[::-1]
    cal = 0
    # ソート（降順)してから累乗をかける
    for i, v in enumerate(cs):
        cal += 2 ** i * v

    return cal
