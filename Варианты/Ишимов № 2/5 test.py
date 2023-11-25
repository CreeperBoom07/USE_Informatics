def f(n):
    s = ''
    while n:
        s = str(n%3) + s
        n //= 3
    return s

n = 16
R = f(n)
if n % 2 == 0:
    R = R.replace('1', '2')
    R = R + R[-2:]
else:
    R = R + str(n%3)*2
print(int(R, 3))
