def to_thee(num):
    s = ''
    while num:
        s = str(num % 3) + s
        num //= 3
    return s


for n in range(1, 1000):
    R = to_thee(n)
    if n % 3 == 0:
        R += R[-2:]
    else:
        R += to_thee((n%3)*5)
    if int(R, 3) > 133:
        print(int(R, 3))
        break

