from string import ascii_uppercase, digits
abc = digits + ascii_uppercase
abc = abc[:23]
for x in abc:
    n1 = int(f'7{x}38596', 23)
    n2 = int(f'14{x}36', 23)
    n3 = int(f'61{x}7', 23)
    if (n1+n2+n3) % 22 == 0:
        print((n1+n2+n3) / 22)
        break
