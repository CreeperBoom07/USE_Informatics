def tr(n):
    s = ''
    while n:
        s = str(n%3) + s
        n //= 3
    return s

for n in range(1, 10000):
    R = tr(n)
    if n % 2 == 0:
        R = '1' + R + '00'
    else:
        R = R + tr(sum(int(x) for x in tr(n)))

    if int(R, 3) > 168:
        print(n)
        break
# 10
