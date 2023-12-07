from fnmatch import *
def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)
for x in range(0, 10**7, 217):
    if fnmatch(str(x), '27?7*'):
        print(x, sum(i for i in f(x) if i%2!=0))
    
