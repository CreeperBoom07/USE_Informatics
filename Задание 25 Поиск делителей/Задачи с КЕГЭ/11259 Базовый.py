from fnmatch import *

for x in range(0, 10**8, 3226):
    if fnmatch(str(x), '3?99?7*8'):
        print(x, x//3226)
##35995708 11158
##36995768 11468
