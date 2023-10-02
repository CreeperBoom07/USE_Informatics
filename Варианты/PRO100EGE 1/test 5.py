def f(n):
    s = ''
    while n:
        s = str(n%6) + s
        n //= 6
    return s

n = 12
R = f(n)
if n % 3 == 0:
    R = R + R[:2]
else:
    R = R + f((n%3)*10)
print(int(R, 6))
