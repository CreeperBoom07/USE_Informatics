from string import ascii_uppercase as UP
abc = '123456789'+ UP
abc = abc[:11]
for x in abc:
    n1 = int(f'3364{x}', 11)
    n2 = int(f'{x}7946', 12)
    n3 = int(f'55{x}87', 14)
    if n1 + n2 == n3:
        print(n3)
        break
