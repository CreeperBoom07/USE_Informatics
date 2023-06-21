alphabet = '0123456789ABCDE'
def f1():
    for x in alphabet:
        if (int(f'123{x}5', 15) + int(f'1{x}233', 15)) % 14 == 0:
            print((int(f'123{x}5', 15) + int(f'1{x}233', 15)) / 14)
            break

def f2():
    for x in range(0, 15):
        num1 = 1 * 15**4 + 2 * 15**3 + 3 * 15**2 + x * 15 + 5
        num2 = 1 * 15**4 + x * 15**3 + 2 * 15**2 + 3 * 15 + 3
        if (num1 + num2) % 14 == 0:
            print((num1 + num2) / 14)
            break


f2()
#  8767
