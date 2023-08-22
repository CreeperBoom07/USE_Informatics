from string import ascii_uppercase

abc = '0123456789' + ascii_uppercase
abc = abc[:18]
for x in abc:
    n1 = int(f'77968{x}11', 18)
    n2 = int(f'4{x}213', 18)
    if (n1+n2) % 7 == 0:
        print((n1+n2) / 7)
        
