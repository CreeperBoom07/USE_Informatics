alphabet = '0123456789ABCDEFG'
for x in alphabet[:15]:
    for y in alphabet:
        if (int(f'123{x}5', 15) + int(f'67{y}9', 17)) % 131 == 0:
            print(int(x, 15), int(y, 17), (int(f'123{x}5', 15) + int(f'67{y}9', 17)) / 131)

# 686
