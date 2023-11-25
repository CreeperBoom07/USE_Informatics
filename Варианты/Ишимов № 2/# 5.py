def f(n):
    s = ''
    while n:
        s = str(n%3) + s
        n //= 3
    return s

for n in range(1, 100000):
    R = f(n)
    if n % 2 == 0:
        R = R.replace('1', '2')
        R = R + R[-2:]
    else:
        R = R + str(n%3)*2
    if int(R, 3) <= 1165:
        print(n)
# 129
