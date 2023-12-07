from fnmatch import *

for x in range(0, 10**9, 17):
    if fnmatch(str(x), '12345?6?8'):
        print(x, x//17)

##for x in range(0, 10**9, 17):
##    s = str(x)
##    if len(s) == 9 and s.startswith('12345') and s[-3] == '6' and s[-1] == '8':
##        print(x,x//17)
