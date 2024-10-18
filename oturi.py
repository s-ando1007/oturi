import math

def y(t, p):
    a = [500, 100, 50, 10]
    z = t - p
    r = {}

    for i in a:
        if z >= i:
            c = z // i
            r[i] = c
            z -= i * c
    
    if r:
        print("おつり:")
        for k, l in r.items():
            print(f"{k}円: {l}枚")
    else:
        print("おつりはないです")

def u(q):
    return q % 10 == 0

n = int(input("支払金額を入力"))
x = int(input("商品金額を入力"))

if u(n) and u(x):
    if n >= x:
        y(n, x)
    else:
        print("金額不足")
else:
    print("支払金額と商品金額は10の倍数で入力してください")