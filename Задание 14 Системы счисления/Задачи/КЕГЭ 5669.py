from string import ascii_uppercase
s = '0123456789' + ascii_uppercase
s = s[:16]
def f(num):
    k = 0
    for i in num:
        if k > 2:
            return False
        if int(i) % 2 == 0:
            k += 1
    return True


for x in s:
    n1 = int(f'8569{x}', 16)
    n2 = int(f'12{x}48', 16)
    total = oct(n1+n2)[2:]
    if f(total):
        print(total)

# 2275735
