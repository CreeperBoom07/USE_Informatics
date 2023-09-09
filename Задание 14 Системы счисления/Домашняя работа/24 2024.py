from string import ascii_uppercase as UP
abc = '0123456789' + UP
abc = abc[:21]
for x in abc:
    for y in abc:
        n1 = int(f'12{y}{x}9', 21)
        n2 = int(f'36{y}99', 21)
        if (n1+n2) % 18 != 0:
            break
    else:
       n1 = int(f'125{x}9', 21)
       n2 = int(f'36599', 21)
       print((n1+n2)/18)
       break
# 47594
        
