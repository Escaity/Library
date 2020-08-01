def pickingNumbers(a):
    n = len(a)
    b = [0] * 101
    for i in a:
        b[i] += 1
    ans = 0
    for j in range(100):
        ans = max(ans, b[j] + b[j + 1])

    return ans