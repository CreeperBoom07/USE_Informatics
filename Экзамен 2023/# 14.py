from string import ascii_lowercase

abc = '0123456789' + ascii_lowercase
abc = abc[:22]
for x in abc:
    n1 = int(f'18{x}89957', 22)
    n2 = int(f'80{x}33', 22)
    n3 = int(f'521{x}6', 22)
    if (n1+n2+n3) % 21 == 0:
        print((n1+n2+n3) / 21)
        break