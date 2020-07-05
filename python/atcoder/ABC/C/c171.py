answer = ""
num = int(input())
i = 0
while num > 0:
    """ 10進数→26進数変換（zの時は例外） """
    i = num % 26
    num //= 26
    if i == 0:
        answer += "z"
        num -= 1
    else:
        answer += chr(96 + i)

print(answer[::-1])

"""　解説
N=int(input())
ans=''
whileN>0:
    N-=1
    ans+=chr(ord('a')+N%26)
    N//=26
    print(ans[::-1])
"""
