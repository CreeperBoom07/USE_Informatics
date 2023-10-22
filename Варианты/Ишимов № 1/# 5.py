def tr(n):
    s = ''
    while n:
        s = str(n%3) + s
        n //= 3
    return s
lst = []
for n in range(1, 10000):
    R = tr(n)
    if sum(int(x) for x in R) % 4 == 0:
        R = '1' +  R
        R = R[:-2]
    else:
        R = R + tr((sum(int(x) for x in R)%4)*3)

    if int(R, 3) > 353:
        lst += [int(R, 3)]

print(min(lst))
# 354
