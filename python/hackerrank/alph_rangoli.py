def print_rangoli(n):
    sq = n
    slh = "-"
    dec = 0
    cnt = 0
    tile = [""] * (sq * 2 - 1)
    if sq == 1:
        return print("a")
    else:
        for i in range(0, sq - 1):
            if i == 0:
                tile[i] += str(slh * (sq * 2 - 2))
                tile[i] += str(chr(96 + sq))
                tile[i] += str(slh * (sq * 2 - 2))
            tile[i + 1] += str(slh * ((sq - 1) * 2 - 2 * i - 2))
            for j in range(0, i + 1):
                tile[i + 1] += str(chr(96 + (sq - j)))
                tile[i + 1] += str(slh)
            tile[i + 1] += str(chr(96 + sq - i - 1))
            dec = -i
            for k in range(0, i + 1):
                tile[i + 1] += str(slh)
                tile[i + 1] += str(chr(96 + (sq + dec + k)))
            tile[i + 1] += str(slh * ((sq - 1) * 2 - 2 * i - 2))
        for i in range(0, sq - 1)[::-1]:
            if i == 0:
                tile[sq + cnt] += str(slh * (sq * 2 - 2))
                tile[sq + cnt] += str(chr(96 + sq))
                tile[sq + cnt] += str(slh * (sq * 2 - 2))
                break
            tile[sq + cnt] += str(slh * ((sq - 1) * 2 - 2 * i))
            for j in range(0, i):
                tile[sq + cnt] += str(chr(96 + (sq - j)))
                tile[sq + cnt] += str(slh)
            tile[sq + cnt] += str(chr(96 + sq - i))
            dec = -j
            for k in range(0, i):
                tile[sq + cnt] += str(slh)
                tile[sq + cnt] += str(chr(96 + (sq + dec + k)))
            tile[sq + cnt] += str(slh * ((sq - 1) * 2 - 2 * i))
            cnt += 1
        return print("\n".join(tile))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
