from string import ascii_uppercase as UP
abc = '0123456789' + UP
m = 100000
m1 = None
for x in abc[:15]:
    for y in abc[:17]:
        n1 = int(f'123{x}5', 15)
        n2 = int(f'67{y}9', 17)
        if (n1 + n2) % 131 == 0:
            print((n1 + n2) / 131, int(x, 15), int(y, 17))
            
