for x in '0123456789ABCDE':
    n1 = int(f'1{x}51', 15)
    n2 = int(f'3{x}2', 15)
    if (n1-n2) % 4 == 0:
        print((n1-n2) / 4)

# 1376
