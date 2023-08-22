def f(s):
    while any(x in s for x in ('25', '355', '555')):
        s = s.replace('25', '32', 1)
        s = s.replace('355', '25', 1)
        s = s.replace('555', '3', 1)
    return s

    
for n in range(11, 1000):
    s = '3' + n*'5'
    if sum([int(num) for num in f(s)]) % 25 == 0:
        print(n)
        break
