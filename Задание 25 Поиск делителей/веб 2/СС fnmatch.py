from fnmatch import *

for x in range(0,10**10, 121):
    if fnmatch(hex(x)[2:], '1?ded?ced'):
        print(x, x//121)
##5065538797 41863957
##6407666925 52955925
##8555171053 70703893
