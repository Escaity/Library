def get_input():
    while True:
        try:
            line = list(input().lower())
            if line == "":
                break
            else:
                yield line
        except EOFError:
            break


s = list(get_input())
s = sum(s, [])
alpha = [0] * 26

for i in s:
    if i.isalpha():
        alpha[ord(*i) - 97] += 1

for i, v in enumerate(alpha):
    print("%s : %d" % (chr(97 + i), v))