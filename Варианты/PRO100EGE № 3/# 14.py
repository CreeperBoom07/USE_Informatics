
abc = '0123456789AB'

for x in abc:
    n1 = int(f'9A87{x}21', 12)
    n2 = int(f'2{x}68', 14)
    n3 = int(f'1{x}2F4', 16)
    if (n1+n2-n3) % 3 == 0:
        print((n1+n2-n3) // 3)
# 9812719
