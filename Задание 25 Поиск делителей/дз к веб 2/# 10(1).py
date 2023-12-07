from fnmatch import *

for x in range(700_000, 700_300):
    if all(not fnmatch(str(x), i) for i in ['*0??3*', '*4??2', '*1*']) and x%13==0:
        print(x, sum(int(i) for i in str(x)))

