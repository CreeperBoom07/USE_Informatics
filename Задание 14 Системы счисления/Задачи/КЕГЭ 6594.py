s = '0123456789ABC'
for x in s:
    n1 = int(f'753{x}2', 13)
    n2 = int(f'2{x}173', 13)
    if (n1+n2) % 12 == 0:
        print((n1+n2) / 12)
        break

# 22953
