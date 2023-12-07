from fnmatch import *


def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return d


for x in range(0, 10**7, 53):
    s = str(x)
    if fnmatch(s, '*2?2*') and s == s[::-1]:
        d = f(x)
        if len(d) > 30:
            print(x, sum(d))

# 212212 508032
# 2527252 5588352
# 4282824 13789440
# 4626264 11787120
# 8125218 19595520
# 8824288 19908504
