from fnmatch import *


for x in range(0, 10**8, 237):
    if fnmatch(str(x), '81?2*80') and not fnmatch(str(x), '*9*'):
        print(x, x//237)
#815280 3440
#8162280 34440
#81324180 343140
#81727080 344840
#81821880 345240        
