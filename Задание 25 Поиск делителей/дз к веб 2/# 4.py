from fnmatch import *

for x in range(0, 10**6, 51):
    if fnmatch(str(x), '12*45*'):
        print(x, x//51)
##122145 2395
##122451 2401
##124542 2442
##124593 2443
##127245 2495
