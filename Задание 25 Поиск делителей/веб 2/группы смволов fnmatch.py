from fnmatch import *

for x in range(0, 10**8, 2023):
    if fnmatch(str(x), '11[02468]??[13579]11'):
        print(x,x//2023)
##11039511 5457
##11444111 5657
##11848711 5857
