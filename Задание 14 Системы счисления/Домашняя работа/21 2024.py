from string import ascii_uppercase as UP
abc = '0123456789' + UP
abc = abc[:17]
for x in abc:
    n1 = int(f'9759{x}', 17)
    n2 = int(f'3{x}108', 17)
    if (n1+n2) % 11 == 0:
        print((n1+n2) / 11)
        break
