def f(s):
    while any(x in s for x in ['52', '2222', '1122']):
        s = s.replace('52', '11')
        s = s.replace('2222', '5')
        s = s.replace('1122', '25')
    return s

for n in range(4, 10_000):
    s = f('5' + n*'2')
    if sum(int(x) for x in s) == 64:
        print(n)
    
# 56
