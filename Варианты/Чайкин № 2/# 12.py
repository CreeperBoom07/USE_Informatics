def prost(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def f(s):
    while any(x in s for x in ('25', '355', '555')):
        s = s.replace('25', '32', 1)
        s = s.replace('355', '25', 1)
        s = s.replace('555', '3', 1)
    return s
k = 0
for n in range(4, 1000):
    s = '3' + n*'5'
    h = sum([int(x) for x in f(s)])
    if prost(h):
        k += 1
print(k)
# 186    
    
    
