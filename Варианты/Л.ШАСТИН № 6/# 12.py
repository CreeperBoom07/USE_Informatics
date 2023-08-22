def f(s):
    while any(x in s for x in ('27', '377', '777')):
        s = s.replace('27', '32', 1)
        s = s.replace('377', '27', 1)
        s = s.replace('777', '3', 1)
    return s



for n in range(10, 100):
    s = '3' + n*'7'
    if sum([int(i) for i in f(s)]) % 22 == 0:
        print(n)
    
