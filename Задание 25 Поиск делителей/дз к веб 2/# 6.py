from fnmatch import *

def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)

for x in range(65001, 10**9):
    d = [i for i in f(x) if i % 2 == 0]
    if len(d) >= 4:
        s = str(x)
        if s[0] == '6' and s[-2] == '5' and '97' in s:
            print(x, sum(d))
##69750 129792
##69752 122080
##69756 139536
##69758 75152
##609750 1103232
##609752 1291248
##609754 630840
