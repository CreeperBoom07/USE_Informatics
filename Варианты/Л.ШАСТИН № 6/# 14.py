from string import ascii_uppercase

abc = '0123456789' + ascii_uppercase
abc = abc[:15]
s = 0
for x in abc:
    num1 = int(f'97968{x}13', 15)
    num2 = int(f'7{x}213', 15)
    if (num1+num2) % 11 == 0:
        s += int(x, 15)
print(s)
