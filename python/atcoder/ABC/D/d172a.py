def sn(n):
    # 等差数列の和
    return n * (n + 1) // 2


def fn(N):
    ans = 0
    for k in range(1, N + 1):
        ans += sn(N // k) * k
    return ans


n = int(input())
ans = fn(n)
print(ans)
