n = int(input())
m = list(map(int, input().split()))
ms = sorted(m)
m_mid = ms[len(ms) // 2]
m_1mid = ms[len(ms) // 2 - 1]
if m_mid == m_1mid:
    print(0)
else:
    print(m_mid - m_1mid)
