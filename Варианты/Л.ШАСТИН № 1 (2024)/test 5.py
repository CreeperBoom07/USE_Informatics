def tr(n):
    s = ''
    while n:
        s = str(n%3) + s
        n //= 3
    return s
n = 12
R = tr(n)
if n % 3 == 0:
    R = R + R[:2]
else:
    R = R + tr((n%3)*5)
print(int(R, 3))
