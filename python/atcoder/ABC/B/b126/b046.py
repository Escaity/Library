N, K = list(map(int, input().split()))
# ボールの塗り方は以下の通り
print(K * (K - 1) ** (N - 1))

"""
10 8
"""
