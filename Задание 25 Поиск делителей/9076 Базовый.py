from fnmatch import *


for n in range(0, 10**9, 2023):
    s = str(n)
    if fnmatch(s, '20*23'):
        sm = sum(int(x) for x in s)
        if sm % 7 == 0 and sm < 20:
            print(n)
#2023
#204323
#2025023
#20232023
#202302023
