def to_three(num: int) -> str:
    s = ''
    while num:
        s = str(num%3) + s
        num //= 3
    return s

lst = []
for n in range(1, 10000):
    n_tr = to_three(n)
    if n % 3 == 0:
        n_tr = '1' + n_tr + '02'
    else:
        n_tr += to_three(n%3*4)
    R = int(n_tr, 3)
    if R < 199:
        lst.append(n)
print(max(lst))
