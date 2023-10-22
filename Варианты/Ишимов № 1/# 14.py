from string import ascii_uppercase as UP
abc = '0123456789' + UP
abc = abc[:26]

for x in abc:
    n1 = int(f'27{x}98876', 26)
    n2 = int(f'26{x}51', 26)
    n3 = int(f'15{x}47', 26)
    n4 = int(f'62{x}5', 26)
    if (n1+n2+n3+n4) % 25 == 0:
        print((n1+n2+n3+n4)//25)
# 739259957
