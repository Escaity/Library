def plusMinus(arr):
    ap = [i for i in arr if i > 0]
    an = [i for i in arr if i < 0]
    az = [i for i in arr if i == 0]
    apl = float(len(ap))
    anl = float(len(an))
    azl = float(len(az))
    arrl = float(len(arr))
    print(apl / arrl)
    print(anl / arrl)
    print(azl / arrl)


"""
LIST = [0, None, 2, 23] → [0, 2, 23]　にしたいときは以下のように書く
l = [i for i in LIST if i is not None]
"""
