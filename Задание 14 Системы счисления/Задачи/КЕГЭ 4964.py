from string import ascii_uppercase
s = '0123456789' + ascii_uppercase
s = s[:21]

for x in range(0, 21):
    for y in range(0, 21):
        X = s[x]
        Y = s[y]
        n1 = int(f'12{y}{x}9', 21)
        n2 = int(f'36{y}99', 21)
        if (n1+n2) % 18 != 0:
            break
    else:
        print((int(f'125{x}9', 21) + int(f'36599', 21))/18)
        break

# 47594
