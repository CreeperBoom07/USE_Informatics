def tr(n):
    s = ''
    while n:
        s = str(n%3) + s
        n //= 3
    return s
lst = []
for n in range(1, 10000):
    R = tr(n)
    if n % 3 == 0:
        R = R + R[:2]
    else:
        R = R + tr((n%3)*5)
    if int(R, 3) > 64:
        lst += [int(R, 3)]
print(min(lst))
# 68
