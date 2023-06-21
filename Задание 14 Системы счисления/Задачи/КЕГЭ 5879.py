'''Запомни уже наконец, ЕСЛИ надо перевести число в с/с с основанием больше чем 10,
   то надо учесть БУКВЫ
'''

def to_13(num):
    alphabet = '0123456789ABC'
    s = ''
    while num:
        s = alphabet[num % 13] + s
        num //= 13
    return s


for x in range(0, 15):
    n1 = 3*15**4 + x*15**3 + 1*15**2 + 5*15 + x
    osn2 = int(f'3{x}51')
    n2 = 1*osn2**2 + 2*osn2 + 3
    n3 = x**x
    osn3 = int(f'1{x}3')
    n4 = 1*osn3**2 + x*osn3 + 3
    osn4 = x+1
    n5 = 1*osn4**2 + x*osn4 + 2
    total = n1+n2+n3+n4+n5
    if total % 13 == 0:
        print(to_13(total))
        break
