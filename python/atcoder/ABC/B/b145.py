n = int(input())
s = input()
s_mae = s[: (n // 2)]
s_ato = s[(n // 2) :]
# print(s_mae, s_ato)
print("Yes") if s_mae == s_ato else print("No")
