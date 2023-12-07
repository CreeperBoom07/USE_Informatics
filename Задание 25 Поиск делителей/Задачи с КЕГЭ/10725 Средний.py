from fnmatch import *

def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i,x//i}
    return sorted(d)

for x in range(65_000, 1_000_000):
    if fnmatch(str(x), '6*97*5?'):
        d = [n for n in f(x) if n % 2 == 0]
        if len(d) >= 4:
            print(x, sum(d))
##69750 129792
##69752 122080
##69756 139536
##69758 75152
##609750 1103232
##609752 1291248
##609754 630840
