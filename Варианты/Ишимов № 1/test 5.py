def tr(n):
    s = ''
    while n:
        s = str(n%3) + s
        n //= 3
    return s


R = tr(16)
if sum(int(x) for x in R) % 4 == 0:
    R = '1' +  R
    R = R[:-2]
else:
    R = R + tr((sum(int(x) for x in R)%4)*3)
print(int(R, 3))
