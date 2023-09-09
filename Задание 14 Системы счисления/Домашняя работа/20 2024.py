from string import ascii_uppercase as UP
abc = '0123456789' + UP
abc = abc[:15]
for x in abc:
    n1 = int(f'123{x}5', 15)
    n2 = int(f'1{x}233', 15)
    if (n1 + n2) % 14 == 0:
        print((n1 + n2) / 14)
        break
# 8767
