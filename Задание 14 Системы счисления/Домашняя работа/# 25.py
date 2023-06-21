from string import ascii_uppercase
alphabet = '0123456789' + ascii_uppercase
alphabet = alphabet[:21]
for x in alphabet:
    for y in alphabet:
        if (int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)) % 18 != 0:
            break
    else:
        print((int(f'125{x}9', 21) + int(f'36599', 21)) / 18)
        break

# 47594
