from string import ascii_uppercase as up

alphabet = '0123456789' + up
alphabet = alphabet[:15]
for x in alphabet:
    n1 = int(f'123{x}5', 15)
    n2 = int(f'1{x}233', 15)
    if (n1+n2) % 14 == 0:
        print((n1+n2) / 14)
        break

# 8767
